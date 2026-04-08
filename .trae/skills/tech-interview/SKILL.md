---
name: "tech-interview"
description: "Generates interview questions for tech stacks (Go, Linux, K8s, Docker, TCP, PostgreSQL, Redis). Invoke when user asks for interview questions, tech interviews, or wants to practice technical questions."
---

# Tech Interview Question Generator

This skill generates comprehensive interview questions based on the content in this repository. It searches through existing interview materials and generates tailored questions for specific technology stacks.

## Supported Technology Stacks

This repository contains interview materials for the following technologies:

- **Go/Golang**: Comprehensive Go language interview questions including concurrency, channels, interfaces, memory management, data structures
- **Linux**: System administration, shell commands, process management, networking
- **Kubernetes (K8s)**: Container orchestration, Pod management, Service networking, deployments, scheduling
- **Docker**: Containerization, images, networking, volumes, best practices
- **TCP/IP**: Network protocols, connection management, HTTP/HTTPS, socket programming
- **PostgreSQL**: Database design, SQL queries, indexing, performance optimization
- **Redis**: Caching strategies, data structures, persistence, clustering
- **Blockchain**: Distributed ledger technology, consensus algorithms, smart contracts, cryptocurrency platforms (Bitcoin, Ethereum), security and cryptography

## How to Use

### Basic Usage

When invoked, this skill will:

1. Search the repository for relevant interview materials based on the specified technology stack
2. Analyze existing content to generate comprehensive interview questions
3. **Format questions in concise mode by default** (question + one-sentence answer)
4. Save generated questions to a markdown file named `题库内容总结-YYYY-MM-DD.md`
5. If detailed mode is requested, provide comprehensive answers with related topics and key points

### Invocation Scenarios

Invoke this skill when:

- User asks "generate interview questions for [technology]"
- User wants to practice "Go/Golang interview questions"
- User needs "Kubernetes interview preparation"
- User asks "help me prepare for a technical interview"
- User wants to know "common [technology] interview questions"
- User asks for "Redis questions for interview"
- User asks for "blockchain interview questions"
- User wants to prepare for "cryptocurrency or blockchain developer interviews"
- User asks about "smart contract questions" or "Ethereum interview preparation"
- User needs "consensus algorithm interview questions"

### Question Generation Process

1. **Search Phase**: Use SearchCodebase and Grep to find relevant files:
   - golang/go-Interview/ for Go questions
   - k8s/ for Kubernetes questions
   - Redis/面经/ for Redis questions
   - mysql/ for database questions
   - 区块链/区块链面经/ for blockchain questions
   - Related markdown files containing technical content

2. **Analysis Phase**: Read and analyze the content to understand:
   - Key concepts and topics
   - Important implementation details
   - Common interview patterns
   - Best practices and pitfalls

3. **Generation Phase**: Generate questions covering:
   - Fundamental concepts
   - Practical implementation
   - Advanced topics
   - Real-world scenarios
   - Common pitfalls and edge cases

### Question Format

Generated interview questions follow this structure by default in **concise mode**:

```markdown
## [Topic/Concept]

**题目**: [Clear, concise question]

**答案**: [One-sentence answer]
```

For detailed mode (when explicitly requested), use the full format:

```markdown
## Question: [Topic/Concept]

### Difficulty: [Basic/Intermediate/Advanced]

### Question:
[Clear, concise question]

### Expected Answer:
[Comprehensive answer based on repository content]

### Related Topics:
- [Related concept 1]
- [Related concept 2]

### Key Points:
- [Important point 1]
- [Important point 2]
```

## Example Usage

### Example 1: Go Interview Questions

User: "Generate Go interview questions about concurrency"

The skill will:
1. Search for Go concurrency-related content in the repository
2. Find relevant files: channel implementations, goroutine patterns, sync primitives
3. Generate questions like:
   - How do goroutines differ from threads?
   - Explain channel buffering and deadlock scenarios
   - How to implement concurrent-safe counters?
   - When would you use sync.Mutex vs channels?

### Example 2: Kubernetes Questions

User: "Help me prepare for K8s interview focusing on networking"

The skill will:
1. Search k8s/ directory for networking content
2. Find k8s面经.md with networking concepts
3. Generate questions about:
   - Pod networking model
   - Service types and use cases
   - Ingress controllers
   - Network policies
   - CNI plugins

### Example 3: Comprehensive Interview Prep

User: "Generate interview questions for all backend technologies"

The skill will:
1. Search across multiple directories
2. Generate questions for:
   - Go (language fundamentals)
   - Redis (caching)
   - PostgreSQL (databases)
   - Docker & K8s (deployment)
   - TCP/IP (networking)

### Example 4: Blockchain Questions

User: "Help me prepare for blockchain developer interview"

The skill will:
1. Search 区块链/区块链面经/ directory for blockchain content
2. Find README.md with blockchain concepts and interview questions
3. Generate questions about:
   - Blockchain fundamentals and architecture
   - Consensus algorithms (PoW, PoS, DPoS)
   - Smart contracts and Ethereum
   - Cryptocurrency and mining
   - Security and cryptography
   - Public vs Private blockchains
   - Distributed ledger technology

## Output File Specification

After generating interview questions, the skill will automatically create a markdown file with the following naming convention:

**Filename Format**: `题库内容总结-YYYY-MM-DD.md`

Where:
- `YYYY` = 4-digit year
- `MM` = 2-digit month (01-12)
- `DD` = 2-digit day (01-31)

Example: `题库内容总结-2026-04-08.md`

**Output Location**: The file will be saved in the same directory where the skill is invoked or in a designated output directory.

**File Content Structure**:
```markdown
# [Technology] Interview Questions

Generated on: YYYY-MM-DD

Total Questions: N

---

## [Topic 1]

**题目**: [Question 1]

**答案**: [One-sentence answer]

---

## [Topic 2]

**题目**: [Question 2]

**答案**: [One-sentence answer]

... (more questions)
```

## Best Practices

### For Interviewers

- Use questions from different difficulty levels
- Mix theoretical and practical questions
- Include scenario-based questions
- Test understanding of trade-offs

### For Candidates

- Study fundamental concepts first
- Understand implementation details
- Practice with real code examples
- Review related topics for depth

## Repository Structure Reference

Key directories for interview materials:

```
golang/go-Interview/
  ├── GOALNG_INTERVIEW_COLLECTION.md  # Comprehensive Go questions
  ├── data-structure/                 # Data structure implementations
  ├── 算法/                            # Algorithm questions
  └── 实战/                            # Practical coding questions

k8s/
  └── k8s面经.md                        # Kubernetes questions

Redis/
  └── 面经/redis面经.md                 # Redis questions

mysql/
  ├── MYSQL知识点整理.md
  └── MySQL索引及优化全总结.md

elasticsearch/
  └── 面经/ES_INTERVIEW_README.md

区块链/
  └── 区块链面经/
      └── README.md                   # Blockchain interview questions
```

## Tips for Effective Use

1. **Be Specific**: Ask for questions on specific topics (e.g., "Go channel questions" vs "all Go questions")
2. **Specify Difficulty**: Ask for "basic", "intermediate", or "advanced" questions
3. **Focus on Weak Areas**: Ask for questions on topics you find challenging
4. **Cross-Reference**: Use related questions to build comprehensive understanding
5. **Practice Answers**: Don't just read questions, practice answering them out loud
6. **Concise Mode**: Questions are generated in concise format by default (question + one-sentence answer) for quick review
7. **Detailed Mode**: Ask for "detailed" or "comprehensive" mode if you need full explanations with related topics and key points
8. **Output Files**: All generated questions are automatically saved to `题库内容总结-YYYY-MM-DD.md` files for easy reference

## Integration with Code

When generating questions that involve code, the skill will:

1. Reference relevant code files in the repository
2. Provide implementation examples
3. Explain code patterns and best practices
4. Point to similar implementations

Example:
```go
// Related implementation in repository:
// golang/go-Interview/channel/channel.go

// Question: How do you implement a worker pool in Go?
// Reference the existing worker pool patterns in the repository
```
