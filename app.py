
"""Streamlit front end for the PDF-first Smart Subject Tutor lab."""

from __future__ import annotations

import os
import time
import streamlit as st

from dotenv import load_dotenv
from pdf_rag import PDFTutor

load_dotenv()

st.set_page_config(
    page_title="Smart Subject Tutor - PDF First",
    layout="wide",
)

st.title("Smart Subject Tutor")
st.caption(
    "Upload PDFs. Ask questions. Get answers with file and page references."
)

DEFAULT_MODELS = {
    "Gemini": "gemini-3.8-flash",
    "OpenAI": "gpt-6-luna",
    "Claude": "claude-haiku-5-5",
}

KEY_NAMES = {
    "Gemini": "GEMINI_API_KEY",
    "OpenAI": "OPENAI_API_KEY",
    "Claude": "ANTHROPIC_API_KEY",
}

# Initialize session state
if "tutor" not in st.session_state:
    with st.spinner(
        "Loading the local PDF search model for the first time..."
    ):
        st.session_state.tutor = PDFTutor()

if "indexed" not in st.session_state:
    st.session_state.indexed = False

if "xp" not in st.session_state:
    st.session_state.xp = 0

if "api_calls" not in st.session_state:
    st.session_state.api_calls = 0

if "last_api_call" not in st.session_state:
    st.session_state.last_api_call = 0.0


# Sidebar: Learning progress and safety limits
with st.sidebar:
    st.header("Learning progress")
    st.metric("Learning XP", st.session_state.xp)

    if st.session_state.xp < 15:
        learner_level = "Beginner"
        st.info(
            "Mode: Beginner - simple explanations and examples"
        )

    elif st.session_state.xp < 40:
        learner_level = "Intermediate"
        st.info(
            "Mode: Intermediate - definitions and exam-style structure"
        )

    else:
        learner_level = "Advanced"
        st.success(
            "Mode: Advanced - trade-offs and deeper reasoning"
        )

    st.divider()

    st.header("App-level safety limits")

    st.write(
        f"API calls this browser session: "
        f"**{st.session_state.api_calls} / 25**"
    )

    st.caption(
        "The app waits 5 seconds between API calls. "
        "Provider-side billing limits must also be set "
        "in your API account."
    )


# 1. Upload subject PDFs
st.subheader("1. Upload your subject PDFs")

uploaded_pdfs = st.file_uploader(
    "Choose one or more PDF files",
    type=["pdf"],
    accept_multiple_files=True,
    help=(
        "Use text-based PDFs with selectable text. "
        "Scanned PDFs need OCR, which is not included "
        "in this starter lab."
    ),
)

if uploaded_pdfs:
    st.write("**Selected files:**")

    for pdf_file in uploaded_pdfs:
        size_mb = pdf_file.size / (1024 * 1024)

        st.write(
            f"- {pdf_file.name} ({size_mb:.1f} MB)"
        )

    index_col, clear_col = st.columns([1, 1])

    # Index selected PDFs
    with index_col:
        if st.button(
            "Index selected PDFs",
            type="primary",
            disabled=not uploaded_pdfs,
        ):
            too_large = [
                f.name
                for f in uploaded_pdfs
                if f.size > 25 * 1024 * 1024
            ]

            if too_large:
                st.error(
                    "For this lab, each PDF must be 25 MB or smaller: "
                    + ", ".join(too_large)
                )

            else:
                with st.spinner(
                    "Reading PDF pages and building the local search index..."
                ):
                    try:
                        stats = st.session_state.tutor.index_pdfs(
                            uploaded_pdfs
                        )

                        st.session_state.indexed = True

                        st.success(
                            f"Ready! Indexed {len(stats['files'])} file(s), "
                            f"{stats['pages_with_text']} text page(s), "
                            f"and {stats['chunks']} searchable passage(s)."
                        )

                        if stats["files_without_text"]:
                            st.warning(
                                "No selectable text was found in: "
                                + ", ".join(
                                    stats["files_without_text"]
                                )
                                + ". These may be scanned PDFs and need OCR."
                            )

                    except Exception as exc:
                        st.session_state.indexed = False
                        st.error(
                            f"PDF indexing failed: {exc}"
                        )

    # Clear current PDF index
    with clear_col:
        if st.button("Clear current PDF index"):
            try:
                existing = (
                    st.session_state.tutor.collection.get(
                        include=["metadatas"]
                    )
                )

                if existing.get("ids"):
                    st.session_state.tutor.collection.delete(
                        ids=existing["ids"]
                    )

                st.session_state.tutor.indexed_files = []
                st.session_state.tutor.indexed_pages = 0
                st.session_state.indexed = False

                st.success(
                    "The current in-memory PDF index has been cleared."
                )

            except Exception as exc:
                st.error(
                    f"Could not clear the index: {exc}"
                )


st.divider()


# 2. Choose AI provider
st.subheader("2. Choose your AI provider")

provider_col, model_col = st.columns([1, 2])

with provider_col:
    provider = st.selectbox(
        "Provider",
        ["Gemini", "OpenAI", "Claude"],
    )

with model_col:
    model = st.text_input(
        "Model ID",
        value=DEFAULT_MODELS[provider],
        key=f"model_id_{provider.lower()}",
        help=(
            "You can change this to any model ID "
            "enabled for your API account."
        ),
    )

st.caption(
    f"The app looks for **{KEY_NAMES[provider]}** in the environment. "
    "It never asks you to paste your key into this page."
)


# 3. Ask a question
st.subheader("3. Ask a question")

question = st.text_area(
    "What would you like to learn from the uploaded PDFs?",
    placeholder=(
        "Example: Explain the four conditions required for a deadlock."
    ),
    height=90,
)

# API cooldown
cooldown_remaining = max(
    0,
    5 - (
        time.time()
        - st.session_state.last_api_call
    ),
)

# Check whether the user can ask a question
can_ask = (
    st.session_state.indexed
    and bool(question.strip())
    and bool(model.strip())
    and st.session_state.api_calls < 25
    and cooldown_remaining <= 0
)


# Ask the tutor
if st.button(
    "Ask the tutor",
    type="primary",
    disabled=not can_ask,
):
    st.session_state.api_calls += 1
    st.session_state.last_api_call = time.time()

    with st.spinner(
        f"Searching your PDFs and asking {provider}..."
    ):
        try:
            answer, sources = st.session_state.tutor.answer(
                question=question.strip(),
                provider=provider,
                model=model.strip(),
                learner_level=learner_level,
                top_k=4,
            )

            # Award learning XP
            st.session_state.xp += 5

            st.markdown("### Tutor's answer")
            st.markdown(answer)

            # Display PDF references
            with st.expander(
                "View the PDF passages used"
            ):
                for idx, item in enumerate(
                    sources,
                    start=1,
                ):
                    st.markdown(
                        f"**{idx}. {item['source']} - "
                        f"page {item['page']}**"
                    )

                    st.write(item["text"])

            st.divider()

            st.caption(
                "+5 XP for asking a learning question. "
                "Teaching depth increases as XP grows."
            )

        except Exception as exc:
            st.error(
                f"The request failed: {exc}"
            )

            st.info(
                "Check that the selected provider's key is configured, "
                "the model ID is correct, your account has API "
                "billing/credits, and the provider has not reached "
                "a usage limit."
            )


# User guidance and API limits
elif not st.session_state.indexed:
    st.info(
        "First upload your PDFs and click **Index selected PDFs**."
    )

elif cooldown_remaining > 0:
    st.warning(
        f"Please wait {cooldown_remaining:.1f} seconds "
        "before the next API request."
    )

elif st.session_state.api_calls >= 25:
    st.warning(
        "This browser session has reached its 25-call safety cap. "
        "Restart the app session to reset this demo counter."
    )


st.divider()


# Privacy reminder
st.caption(
    "Privacy reminder: PDF text passages retrieved by this app "
    "are sent to the selected AI provider for answering. "
    "Do not upload confidential or restricted documents "
    "unless you have permission."
)
