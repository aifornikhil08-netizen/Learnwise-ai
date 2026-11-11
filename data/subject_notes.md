# Operating Systems – Subject Knowledge Base
## B.Tech CSE Core | RAG Dataset

**Subject:** Operating Systems  
**Level:** Undergraduate (B.Tech CSE)  
**Dataset Version:** 1.0  
**Purpose:** Retrieval-Augmented Generation (RAG) for an AI Subject Tutor.

---

# TOPIC 1: PROCESS VS THREAD

## Chunk 1.1 – Introduction to Process

A process is a program that is currently being executed by the CPU. It is an active entity that contains program instructions, data, memory, and other resources required for execution.

Every process has its own virtual address space and operating system resources.

### Main Components of a Process

1. **Code Segment:** Contains the executable instructions of a program.
2. **Data Segment:** Stores global and static variables.
3. **Heap:** Stores dynamically allocated memory.
4. **Stack:** Stores local variables, function parameters, and function call information.
5. **Process Control Block (PCB):** Stores information about the process, such as process ID, process state, CPU registers, scheduling information, and memory information.

### Example

When a user opens Google Chrome, the operating system creates one or more processes to run the application.

Each process has its own execution environment and associated resources.

## Chunk 1.2 – Introduction to Thread

A thread is the smallest unit of CPU execution within a process.

A process can contain one or multiple threads. Multiple threads belonging to the same process share code, data, and heap memory.

However, every thread has its own:
- Stack.
- Program Counter.
- CPU Registers.
- Thread ID.

Threads are also called lightweight processes because creating and switching between threads is generally less expensive than doing so between separate processes.

### Example

A web browser may use different threads for:
- Loading web pages.
- Playing videos.
- Handling user input.
- Downloading files.

These activities can happen concurrently.

## Chunk 1.3 – Difference Between Process and Thread

| Basis | Process | Thread |
|---|---|---|
| Definition | Program in execution | Smallest unit of execution |
| Memory | Separate virtual address space | Shares process memory |
| Communication | Requires IPC mechanisms | Can communicate through shared memory |
| Creation | Generally slower | Generally faster |
| Context switching | Generally more expensive | Generally less expensive |
| Resource sharing | More isolated | Shares code, data and heap |
| Failure impact | Usually isolated from other processes | May affect the entire process |
| Security | Better isolation | Less isolation |
| Stack | Has its own stack | Every thread has its own stack |

## Chunk 1.4 – Process Control Block (PCB)

A Process Control Block is a data structure maintained by the operating system to store information about a process.

### Important PCB Information

1. Process ID (PID).
2. Process State.
3. Program Counter.
4. CPU Registers.
5. CPU Scheduling Information.
6. Memory Management Information.
7. I/O Status Information.
8. Accounting Information.

### Importance of PCB

The operating system uses the PCB to manage processes and perform context switching.

## Chunk 1.5 – Context Switching

Context switching is the process of saving the current execution state of one process or thread and loading the execution state of another.

### Steps

1. The CPU stops executing the current process.
2. The operating system saves its CPU registers and program counter.
3. The saved state is stored in the appropriate process or thread control structure.
4. The scheduler selects another process or thread.
5. The operating system restores its execution state.
6. The CPU resumes execution.

### Types

- Process Context Switching: Switching from one process to another.
- Thread Context Switching: Switching between threads.

Process switching generally involves more overhead because address-space and resource-management state may need to change. However, neither process nor thread switching necessarily requires flushing the entire CPU cache or all TLB entries. Modern processors use mechanisms such as Address Space Identifiers (ASIDs) to reduce this overhead.

## Chunk 1.6 – Inter-Process Communication (IPC)

Inter-Process Communication refers to mechanisms that allow separate processes to exchange information and coordinate their activities.

### Common IPC Methods

1. **Shared Memory:** Multiple processes access a common memory region.
2. **Message Passing:** Processes communicate by sending and receiving messages.
3. **Pipes:** Provide a communication channel between processes.
4. **Sockets:** Allow communication between processes on the same or different computers.
5. **Signals:** Notify a process that a particular event has occurred.

## Chunk 1.7 – Advantages and Disadvantages

### Process Advantages
- Provides memory isolation.
- Offers better fault isolation.
- Supports independent program execution.
- Improves security between applications.

### Process Disadvantages
- Higher creation overhead.
- More expensive context switching.
- IPC can be more complicated.

### Thread Advantages
- Faster creation and termination in many systems.
- Efficient resource sharing.
- Lower communication overhead within a process.
- Supports concurrent activities.

### Thread Disadvantages
- Synchronization is required.
- Shared memory can cause race conditions.
- One faulty thread can affect the entire process.
- Debugging concurrent programs can be difficult.

## Chunk 1.8 – Important Questions and Answers

**Q1. What is a process?**

A process is a program currently executing in the computer. It has its own virtual address space and resources.

**Q2. What is a thread?**

A thread is the smallest unit of CPU execution within a process. It shares process resources but has its own stack and CPU registers.

**Q3. Why are threads called lightweight processes?**

Threads are called lightweight processes because they generally require fewer resources to create and switch than independent processes.

**Q4. What is context switching?**

Context switching is the process of saving the state of one executing process or thread and restoring another so that the CPU can execute it.

**Q5. What is PCB?**

PCB stands for Process Control Block. It stores important information about a process, including its ID, state, registers, and scheduling information.

**Q6. What is the main difference between a process and a thread?**

A process has its own virtual address space, whereas threads within the same process share memory and resources.

**Q7. Can two threads share memory?**

Yes. Threads belonging to the same process share code, data, and heap memory.

**Q8. What happens if one thread crashes?**

A serious failure in one thread can terminate or corrupt the entire process because threads share the same address space.

---

# TOPIC 2: DEADLOCK AND FOUR COFFMAN CONDITIONS

## Chunk 2.1 – Introduction to Deadlock

A deadlock is a situation in an operating system where two or more processes become permanently blocked because each process is waiting for a resource held by another process in the same group.

As a result, none of the processes can continue execution.

### Real-Life Example

Imagine two people:

- Person A holds a pen and needs a notebook.
- Person B holds a notebook and needs a pen.

Person A waits for the notebook, while Person B waits for the pen.

Neither person releases their resource. This situation represents a deadlock.

## Chunk 2.2 – Resource in Operating Systems

A resource is anything required by a process to perform its task.

### Types of Resources

1. Hardware Resources:
   - Printer.
   - CPU devices.
   - Memory.
   - Disk drives.

2. Software Resources:
   - Files.
   - Database locks.
   - Semaphores.
   - Mutex locks.

A process must request a resource, use it, and release it after completing its task.

## Chunk 2.3 – Four Coffman Conditions

A deadlock can occur only when all four Coffman conditions are present simultaneously.

### 1. Mutual Exclusion

At least one resource must be non-shareable.

Only one process can use that resource at a time.

Example: A printer being used by one process cannot simultaneously be used by another process in an exclusive printing operation.

### 2. Hold and Wait

A process must hold at least one resource while waiting to acquire another resource.

Example:
- Process P1 holds a printer.
- Process P1 requests a scanner.
- The scanner is currently unavailable.

P1 continues holding the printer while waiting for the scanner.

### 3. No Preemption

A resource cannot be forcibly taken away from a process.

The process must release the resource voluntarily after completing its task.

Example: The operating system cannot simply take an exclusively locked resource away from a process without considering its consistency and recovery requirements.

### 4. Circular Wait

A circular chain of processes exists where each process waits for a resource held by the next process.

Example:

- P1 waits for a resource held by P2.
- P2 waits for a resource held by P3.
- P3 waits for a resource held by P1.

This creates a circular waiting condition.

## Chunk 2.4 – Example of Deadlock

Consider two processes and two resources:

- Process P1 holds Resource R1 and requests R2.
- Process P2 holds Resource R2 and requests R1.

Neither process can continue.

### Resource Allocation Representation

P1 → R2 → P2 → R1 → P1

This forms a circular wait.

Therefore, both processes remain blocked.

## Chunk 2.5 – Methods of Handling Deadlock

There are four common approaches to handling deadlocks.

### 1. Deadlock Prevention

Deadlock prevention ensures that at least one of the four Coffman conditions cannot occur.

Examples:
- Make resources shareable where possible.
- Require processes to request all resources together.
- Allow resource preemption where safe.
- Enforce a fixed resource ordering.

### 2. Deadlock Avoidance

Deadlock avoidance checks whether granting a resource request will keep the system in a safe state.

The Banker’s Algorithm is a famous deadlock avoidance algorithm.

### 3. Deadlock Detection

The operating system allows deadlocks to occur and periodically checks whether a deadlock exists.

Resource Allocation Graphs and detection algorithms can help identify deadlocks.

### 4. Deadlock Recovery

After detecting a deadlock, the operating system can recover by:

- Terminating one or more processes.
- Taking resources away when safe and possible.
- Rolling back processes to an earlier safe state.

## Chunk 2.6 – Safe State and Unsafe State

**Safe State:** A system is in a safe state if there exists at least one sequence in which all processes can complete using the available resources.

**Unsafe State:** A system is in an unsafe state if no safe execution sequence can be guaranteed.

Important: An unsafe state does not necessarily mean that a deadlock has already occurred.

## Chunk 2.7 – Advantages of Deadlock Prevention

- Avoids permanent process blocking.
- Improves system reliability.
- Helps maintain resource availability.
- Makes system behavior more predictable.

## Chunk 2.8 – Important Questions and Answers

**Q1. What is deadlock?**

Deadlock is a situation where two or more processes wait indefinitely for resources held by one another.

**Q2. What are the four Coffman conditions?**

1. Mutual Exclusion.
2. Hold and Wait.
3. No Preemption.
4. Circular Wait.

**Q3. What is Mutual Exclusion?**

It means that a resource can be used by only one process at a time.

**Q4. What is Hold and Wait?**

It means a process holds one resource while waiting for another resource.

**Q5. What is Circular Wait?**

It is a situation where processes form a circular chain of resource dependencies.

**Q6. What is Deadlock Prevention?**

Deadlock prevention is a technique that ensures at least one necessary deadlock condition cannot occur.

**Q7. What is the Banker’s Algorithm?**

The Banker’s Algorithm is a deadlock avoidance algorithm that checks whether granting a resource request keeps the system in a safe state.

**Q8. Is every unsafe state a deadlock?**

No. An unsafe state means that safe completion cannot be guaranteed, but a deadlock may not have occurred yet.

**Q9. Can deadlock occur without circular wait?**

No. Circular wait is one of the necessary conditions for deadlock.

---

# TOPIC 3: VIRTUAL MEMORY, PAGING AND PAGE FAULTS

## Chunk 3.1 – Introduction to Virtual Memory

Virtual Memory is a memory management technique that allows a process to use a large virtual address space even when physical RAM is limited.

It creates the illusion that every process has its own large and continuous memory space.

The operating system and hardware manage the mapping between virtual addresses and physical memory.

### Advantages

- Allows programs larger than available RAM to execute.
- Supports multiple processes.
- Provides memory isolation.
- Improves memory utilization.
- Simplifies memory management for applications.

## Chunk 3.2 – Introduction to Paging

Paging is a memory management technique that divides virtual memory and physical memory into fixed-size blocks.

### Important Terms

**Page:** A fixed-size block of virtual memory.

**Frame:** A fixed-size block of physical RAM.

**Page Table:** A data structure that maps virtual pages to physical memory frames.

Pages and frames have the same size.

A common page size is 4 KB, although modern systems support other page sizes.

### Example

Suppose:
- Page size = 4 KB.
- Virtual memory contains 4 pages.
- Physical RAM has 8 available frames.

The operating system can load virtual pages into different physical frames. They do not need to be stored in consecutive frames.

## Chunk 3.3 – Page Table

A page table is a data structure maintained by the operating system and used by the Memory Management Unit (MMU) to translate virtual addresses into physical addresses.

### Working

1. CPU generates a virtual address.
2. MMU identifies the virtual page number.
3. The page table is checked.
4. The corresponding physical frame number is obtained.
5. The physical address is generated.

If the page is not currently mapped to physical memory, a page fault may occur.

### Page Table Entry Information

A page table entry can contain:

- Physical frame number.
- Present or valid bit.
- Read/write permissions.
- User/supervisor permissions.
- Accessed bit.
- Dirty bit.

## Chunk 3.4 – Memory Management Unit (MMU)

The Memory Management Unit is a hardware component responsible for translating virtual addresses into physical addresses.

### Functions

1. Address translation.
2. Memory protection.
3. Access permission checking.
4. Supporting virtual memory.
5. Working with page tables.

The MMU helps ensure that processes access only permitted memory locations.

## Chunk 3.5 – Translation Lookaside Buffer (TLB)

The Translation Lookaside Buffer is a small, fast hardware cache that stores recently used virtual-to-physical address translations.

### Working

1. CPU generates a virtual address.
2. MMU checks the TLB.
3. If the translation is found, it is called a TLB hit.
4. If the translation is missing, it is called a TLB miss.
5. The system checks the page table and obtains the translation.
6. The translation may be stored in the TLB for future use.

### Difference Between TLB Hit and TLB Miss

**TLB Hit:** Required address translation is found in the TLB.

**TLB Miss:** Required translation is not found in the TLB, so the page table must be consulted.

A TLB miss is not the same as a page fault.

## Chunk 3.6 – Page Fault

A page fault occurs when a process accesses a virtual memory page that is not currently available in physical memory, or when an access violates memory permissions.

A page fault causes the CPU to transfer control to the operating system through an exception.

### Steps of Page Fault Handling

1. CPU attempts to access a virtual memory page.
2. Hardware detects that the page is not present or that access is invalid.
3. A page fault exception occurs.
4. The operating system checks whether the memory access is valid.
5. If valid, the OS locates the required page.
6. If necessary, the OS selects a free frame or replaces an existing page.
7. The required page is loaded into RAM.
8. The page table is updated.
9. The interrupted instruction is restarted.

If the memory access is invalid, the operating system may terminate the process or report a memory access error.

### Example

Suppose a program requires a page that is stored on disk but not currently loaded in RAM.

The OS loads that page into physical memory and allows the program to continue.

## Chunk 3.7 – Page Replacement Algorithms

When RAM is full and a new page must be loaded, the operating system may need to replace an existing page.

### 1. FIFO (First In First Out)

The oldest loaded page is removed first.

Advantage: Simple to implement.

Disadvantage: May remove frequently used pages and can exhibit Belady's anomaly.

### 2. LRU (Least Recently Used)

The page that has not been used for the longest time is replaced.

Advantage: Uses recent usage history.

Disadvantage: Maintaining accurate usage information can be expensive.

### 3. Optimal Page Replacement

Replaces the page that will not be used for the longest time in the future.

Advantage: Produces the minimum possible number of page faults for a given reference string.

Disadvantage: Requires knowledge of future memory references, so it is mainly used as a theoretical benchmark.

## Chunk 3.8 – Thrashing

Thrashing is a condition where the operating system spends more time handling page faults and transferring pages between RAM and secondary storage than executing actual instructions.

### Causes

- Insufficient physical RAM.
- Too many active processes.
- Excessive page faults.
- Poor memory allocation.
- High memory demand.

### Effects

- Very slow system performance.
- High disk activity.
- Low CPU utilization.
- Increased response time.

### Solutions

- Increase physical RAM.
- Reduce the number of active processes.
- Improve memory allocation.
- Use working-set or page-fault-frequency techniques.
- Reduce excessive memory demands.

## Chunk 3.9 – Difference Between Paging and Segmentation

| Basis | Paging | Segmentation |
|---|---|---|
| Division | Fixed-size blocks | Variable-size blocks |
| Block name | Page | Segment |
| Memory size | Equal-sized pages | Different-sized segments |
| Fragmentation | Internal fragmentation may occur | External fragmentation may occur |
| Address | Page number + offset | Segment number + offset |
| Main purpose | Efficient memory allocation | Logical division of programs |

## Chunk 3.10 – Important Questions and Answers

**Q1. What is virtual memory?**

Virtual memory is a memory management technique that allows programs to use a virtual address space larger than the available physical RAM.

**Q2. What is paging?**

Paging divides virtual memory into fixed-size pages and physical memory into equal-size frames.

**Q3. What is a page table?**

A page table stores mappings between virtual pages and physical memory frames.

**Q4. What is a page fault?**

A page fault occurs when a required virtual memory page is unavailable in physical memory or when an invalid memory access occurs.

**Q5. What is a frame?**

A frame is a fixed-size block of physical RAM.

**Q6. What is MMU?**

MMU stands for Memory Management Unit. It translates virtual addresses into physical addresses.

**Q7. What is TLB?**

TLB stands for Translation Lookaside Buffer. It stores recently used address translations to speed up memory access.

**Q8. What is thrashing?**

Thrashing occurs when the system spends too much time transferring pages between RAM and disk instead of executing programs.

**Q9. What is page replacement?**

Page replacement is the process of removing an existing page from RAM to make space for a required page.

**Q10. Name three page replacement algorithms.**

FIFO, LRU, and Optimal Page Replacement.

**Q11. Is a TLB miss always a page fault?**

No. A TLB miss means the translation is not in the TLB. The page may still be present in RAM and can be found through the page table.

---

# TOPIC 4: CPU SCHEDULING ALGORITHMS

## Chunk 4.1 – Introduction to CPU Scheduling

CPU Scheduling is the process by which the operating system selects a process from the Ready Queue and allocates the CPU to it.

The main objective is to use the CPU efficiently and provide good system performance.

### Objectives

1. Maximize CPU utilization.
2. Maximize throughput.
3. Minimize waiting time.
4. Minimize turnaround time.
5. Minimize response time.
6. Provide fairness among processes.

## Chunk 4.2 – Important Scheduling Terms

**Arrival Time (AT):** Time when a process enters the ready queue.

**Burst Time (BT):** Total CPU execution time required by a process.

**Completion Time (CT):** Time when a process finishes execution.

**Turnaround Time (TAT):** Total time between arrival and completion.

Formula:

TAT = Completion Time - Arrival Time

**Waiting Time (WT):** Total time a process spends waiting in the ready queue.

Formula:

WT = Turnaround Time - Burst Time

**Response Time (RT):** Time between process arrival and its first CPU allocation.

Formula:

RT = First CPU Start Time - Arrival Time

**Time Quantum:** A fixed amount of CPU time allocated to a process in Round Robin scheduling.

## Chunk 4.3 – First Come First Served (FCFS)

FCFS is a non-preemptive CPU scheduling algorithm.

The process that arrives first gets the CPU first.

It follows the FIFO (First In First Out) queue principle.

### Working

1. Processes enter the ready queue.
2. The scheduler selects the first process.
3. The process gets the CPU.
4. It executes until completion or blocking.
5. The next process gets the CPU.

### Example

Consider these processes:

| Process | Arrival Time | Burst Time |
|---|---:|---:|
| P1 | 0 | 5 |
| P2 | 1 | 3 |
| P3 | 2 | 2 |

Gantt Chart:

| P1 | P2 | P3 |
|---|---|---|
| 0–5 | 5–8 | 8–10 |

Completion Times:
- P1 = 5
- P2 = 8
- P3 = 10

Turnaround Times:
- P1 = 5 - 0 = 5
- P2 = 8 - 1 = 7
- P3 = 10 - 2 = 8

Waiting Times:
- P1 = 5 - 5 = 0
- P2 = 7 - 3 = 4
- P3 = 8 - 2 = 6

Average Waiting Time:

(0 + 4 + 6) / 3 = 3.33 milliseconds.

### Advantages

- Simple to understand.
- Easy to implement.
- Fair according to arrival order.
- No starvation due to later arrivals.

### Disadvantages

- Can produce high average waiting time.
- Short processes may wait behind long processes.
- Not suitable for interactive systems.

### Convoy Effect

The convoy effect occurs when short processes wait behind a long CPU-bound process.

It can increase average waiting time and reduce overall system efficiency.

## Chunk 4.4 – Shortest Job First (SJF)

SJF is a CPU scheduling algorithm that selects the process with the smallest next CPU burst time.

In its basic form, SJF is non-preemptive.

### Working

1. The scheduler checks the available processes.
2. It compares their CPU burst times.
3. It selects the process with the shortest burst.
4. The selected process executes until completion.
5. The scheduler selects the next shortest available process.

### Example

Consider three processes that arrive at time 0:

| Process | Burst Time |
|---|---:|
| P1 | 6 |
| P2 | 2 |
| P3 | 4 |

Execution Order:

P2 → P3 → P1

Gantt Chart:

| P2 | P3 | P1 |
|---|---|---|
| 0–2 | 2–6 | 6–12 |

Completion Times:
- P1 = 12
- P2 = 2
- P3 = 6

Waiting Times:
- P1 = 12 - 6 = 6
- P2 = 2 - 2 = 0
- P3 = 6 - 4 = 2

Average Waiting Time:

(6 + 0 + 2) / 3 = 2.67 milliseconds.

### Advantages

- Minimizes average waiting time under standard assumptions when burst times are known.
- Gives priority to shorter processes.
- Efficient for batch processing.

### Disadvantages

- CPU burst time is difficult to predict accurately.
- Long processes may experience starvation.
- Requires knowledge or estimation of burst times.

### Starvation in SJF

Starvation occurs when a process waits for a very long time because shorter processes keep getting selected before it.

### Preemptive SJF (Shortest Remaining Time First)

Shortest Remaining Time First (SRTF) is the preemptive version of SJF.

If a new process arrives with a shorter remaining burst time than the currently running process, the CPU can be allocated to the new process.

## Chunk 4.5 – Round Robin (RR)

Round Robin is a preemptive CPU scheduling algorithm mainly used in time-sharing systems.

Each process receives a fixed amount of CPU time called a Time Quantum.

If a process does not finish within its allocated quantum, it is preempted and moved to the end of the ready queue.

### Working

1. Processes enter the ready queue.
2. The first process gets the CPU.
3. It executes for one time quantum or until completion.
4. If unfinished, it moves to the back of the queue.
5. The next process gets the CPU.
6. The process repeats until all processes finish.

### Example

Consider:

Time Quantum = 2 milliseconds.

| Process | Burst Time |
|---|---:|
| P1 | 5 |
| P2 | 3 |
| P3 | 1 |

All processes arrive at time 0.

### Execution

- P1 executes from 0–2. Remaining time = 3.
- P2 executes from 2–4. Remaining time = 1.
- P3 executes from 4–5. Process completes.
- P1 executes from 5–7. Remaining time = 1.
- P2 executes from 7–8. Process completes.
- P1 executes from 8–9. Process completes.

### Gantt Chart

P1 | P2 | P3 | P1 | P2 | P1

0–2 | 2–4 | 4–5 | 5–7 | 7–8 | 8–9

Completion Times:
- P1 = 9
- P2 = 8
- P3 = 5

Turnaround Times:
- P1 = 9
- P2 = 8
- P3 = 5

Waiting Times:
- P1 = 9 - 5 = 4
- P2 = 8 - 3 = 5
- P3 = 5 - 1 = 4

Average Waiting Time:

(4 + 5 + 4) / 3 = 4.33 milliseconds.

### Advantages

- Fair CPU allocation.
- Suitable for time-sharing systems.
- Good response time with an appropriate time quantum.
- Prevents indefinite CPU occupation by one process.

### Disadvantages

- Too small a time quantum increases context-switching overhead.
- Too large a time quantum makes it behave more like FCFS.
- Average waiting time can be higher than SJF.
- Choosing the correct time quantum is important.

## Chunk 4.6 – Comparison of FCFS, SJF and Round Robin

| Feature | FCFS | SJF | Round Robin |
|---|---|---|---|
| Full Form | First Come First Served | Shortest Job First | Round Robin |
| Type | Non-preemptive | Basic version non-preemptive | Preemptive |
| Selection | Arrival order | Shortest CPU burst | Circular ready queue |
| Starvation | No, under normal assumptions | Possible | Generally avoided |
| Complexity | Low | Moderate | Moderate |
| Main Problem | Convoy effect | Starvation | Context-switching overhead |
| Best Use | Simple batch systems | Short-job-oriented scheduling | Interactive systems |

## Chunk 4.7 – Important CPU Scheduling Formulas

1. Turnaround Time:

TAT = CT - AT

2. Waiting Time:

WT = TAT - BT

3. Average Waiting Time:

Average WT = Sum of all waiting times / Number of processes

4. Average Turnaround Time:

Average TAT = Sum of all turnaround times / Number of processes

5. Response Time:

RT = First CPU Start Time - Arrival Time

## Chunk 4.8 – Important Questions and Answers

**Q1. What is CPU scheduling?**

CPU scheduling is the process of selecting a process from the ready queue and allocating the CPU to it.

**Q2. What is FCFS?**

FCFS is a non-preemptive scheduling algorithm in which the process that arrives first gets the CPU first.

**Q3. What is SJF?**

SJF selects the process with the smallest CPU burst time.

**Q4. What is Round Robin?**

Round Robin is a preemptive scheduling algorithm in which every process gets a fixed amount of CPU time called a time quantum.

**Q5. What is a time quantum?**

A time quantum is the fixed amount of CPU time allocated to a process during one turn in Round Robin scheduling.

**Q6. What is the convoy effect?**

The convoy effect occurs when short processes wait behind a long process, increasing average waiting time.

**Q7. What is starvation?**

Starvation occurs when a process waits indefinitely because other processes continuously receive resources or CPU time before it.

**Q8. Which scheduling algorithm is suitable for interactive systems?**

Round Robin is suitable for interactive and time-sharing systems.

**Q9. Which algorithm minimizes average waiting time under standard assumptions?**

Shortest Job First minimizes average waiting time when CPU burst times are known and the standard scheduling assumptions apply.

**Q10. What is the difference between preemptive and non-preemptive scheduling?**

In preemptive scheduling, the OS can take the CPU away from a running process. In non-preemptive scheduling, a process keeps the CPU until it finishes its CPU burst or blocks.

---

# FINAL REVISION SECTION

## Important Definitions

1. Process: A program in execution.
2. Thread: The smallest unit of CPU execution.
3. PCB: Data structure containing process information.
4. Context Switching: Saving and restoring CPU execution state.
5. Deadlock: Processes waiting indefinitely for resources held by one another.
6. Mutual Exclusion: A resource can be used by only one process at a time.
7. Virtual Memory: Technique that provides a virtual address space.
8. Paging: Dividing memory into fixed-size pages and frames.
9. Page Fault: Exception caused by an unavailable page or invalid memory access.
10. Thrashing: Excessive paging that severely reduces system performance.
11. CPU Scheduling: Selecting a process for CPU execution.
12. FCFS: Scheduling based on arrival order.
13. SJF: Scheduling based on the shortest CPU burst.
14. Round Robin: Scheduling using a fixed time quantum.

## Important Comparisons for Exams

1. Process vs Thread.
2. Preemptive vs Non-preemptive Scheduling.
3. Paging vs Segmentation.
4. TLB Hit vs TLB Miss.
5. Deadlock Prevention vs Avoidance.
6. FCFS vs SJF.
7. SJF vs Round Robin.
8. Page Fault vs TLB Miss.

## Important Numerical Topics

1. FCFS scheduling calculations.
2. SJF scheduling calculations.
3. Round Robin scheduling calculations.
4. Average Waiting Time.
5. Average Turnaround Time.
6. Page Replacement Algorithms (FIFO, LRU, Optimal).
7. Page number and offset calculations.

## RAG Retrieval Keywords

process, thread, PCB, process control block, context switching, shared memory, IPC, deadlock, Coffman conditions, mutual exclusion, hold and wait, no preemption, circular wait, Banker algorithm, deadlock prevention, deadlock avoidance, virtual memory, paging, page table, frame, page, MMU, TLB, page fault, page replacement, FIFO, LRU, optimal replacement, thrashing, CPU scheduling, FCFS, SJF, SRTF, Round Robin, time quantum, burst time, arrival time, completion time, turnaround time, waiting time, response time, convoy effect, starvation.

---

**END OF OPERATING SYSTEMS DATASET**