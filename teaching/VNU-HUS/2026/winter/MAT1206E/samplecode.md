---
layout: default
title: "VNU-HUS MAT1206E - Sample Code"
last_modified_at: 2026-09-01
lang: "en"
katex: true
---

<div class="alert alert-info" markdown="1">

This page provides sample programs for selected examples described in Wolfgang Ertel's *Introduction to Artificial Intelligence*. The programs are intended only for running and comparing their output with the corresponding descriptions in the book.

* TOC
{:toc}

</div>

# Create a GitHub Codespace

The required programs are already installed in the development environment of the public repository [VNU-HUS-IntroAI-Exercises](https://github.com/hoanganhduc/VNU-HUS-IntroAI-Exercises).

1. Open [Create a codespace for VNU-HUS-IntroAI-Exercises](https://codespaces.new/hoanganhduc/VNU-HUS-IntroAI-Exercises?quickstart=1).
2. Select **Create codespace** and wait until the Codespace is ready.
3. Open a terminal in the Codespace.

# Chapter 3: First-order predicate logic

The file `chapter3.zip` contains the following files:

| **File** | **Description** |
|:---------|:----------------|
| `halbgr1.lop` | Solving the mathematical example in Section 3.7 by the E theorem prover |
| `halbgr2.lop` | Improving `halbgr1.lop` by using the power of the built-in "equality" in E instead of the predicate `eq` |
| `proof.sh` | All `*.lop` files are for the E theorem prover and can be run with the command `bash proof.sh <filename>`. |

## Download the sample code

Create a directory for the sample code, change to that directory, and download the ZIP file for Chapter 3 from this course website:

```bash
mkdir -p ~/MAT1206E/samplecode
cd ~/MAT1206E/samplecode
wget -nc https://hoanganhduc.github.io/teaching/VNU-HUS/2026/winter/MAT1206E/samplecode/chapter3.zip
```

Extract the ZIP file:

```bash
unzip -o chapter3.zip
```

The ZIP file can also be downloaded directly: [chapter3.zip](https://hoanganhduc.github.io/teaching/VNU-HUS/2026/winter/MAT1206E/samplecode/chapter3.zip).

## Run the sample code

Change to the directory containing the Chapter 3 files before running them:

```bash
cd ~/MAT1206E/samplecode/chapter3
```

The script `proof.sh` is a wrapper for `eprover`. When it receives the name of a `.lop` file, it runs:

```bash
eprover --proof-object <filename> | epclextract
```

The option `--proof-object` asks E to include a proof object in its output. The pipe sends that output to `epclextract`, which extracts the generated proof. Therefore, `proof.sh` does not implement a separate prover; it provides a shorter way to run the same `eprover` and `epclextract` pipeline.

### Method 1: Run through `proof.sh`

```bash
bash proof.sh halbgr1.lop
bash proof.sh halbgr2.lop
```

### Method 2: Run `eprover` directly

```bash
eprover --proof-object halbgr1.lop | epclextract
eprover --proof-object halbgr2.lop | epclextract
```

The first file represents equality by the predicate `eq`; the second uses the built-in equality of E. Compare the generated proofs with the discussion in Section 3.7 of the book. The command described as `eproof` in the book is no longer available.

# Chapter 5: Logic programming with PROLOG

The file `chapter5.zip` contains the following files:

| **Files** | **Description** |
|:----------|:----------------|
| `rel.pl`, `rel01.pl`, `rel02.pl` | Different versions of a PROLOG program to solve the family relationships example (Section 5.2). The first version is `rel.pl`. Line 8 of this version, `child(X,Z,Y) :- child(X,Y,Z).`, is a recursive definition which may cause the program to run forever. In `rel01.pl`, this issue is resolved, but the new issue is that the symmetry of `child` as described in line 8 before is no longer given. The final version `rel02.pl` resolves both issues. |
| `max.pl`, `maxwCut.pl` | Illustrating the cut operation in PROLOG (Section 5.3) |
| `append.pl` | A PROLOG implementation of the predicate `append(X, Y, Z)` that appends the list `Y` to the list `X` and saves the result to the list `Z` (Section 5.4) |
| `nrev.pl`, `accrev.pl` | Two PROLOG implementations for the task of reversing a list. `nrev.pl` is an implementation of the naive reverse algorithm---which is very inefficient due to calling `append`. `accrev.pl` is a more efficient implementation using a temporary store, known as the *accumulator* (Section 5.4) |
| `dynamic_rel.pl` | A dynamic version of the PROLOG program used in the family relationships example. This is an example illustrating the use of the built-in `asserta` PROLOG predicate to insert the derived facts to the beginning of the knowledge base to avoid a repeated derivation |
| `plan.pl`, `plan1.pl` | Fig. 5.4, the first version of a PROLOG program to solve the famous farmer-wolf-goat-cabbage problem. `plan1.pl` is the same as `plan.pl` but having extra comments to explain the code in details |
| `raumplan.pl` | Fig. 5.5, A GNU-PROLOG program for solving the room scheduling problem in Example 5.2. This is also an example illustrating the use of *Constraint Logic Programming (CLP)* |

## Download the sample code

Create a directory for the sample code, change to that directory, and download the ZIP file for Chapter 5 from this course website:

```bash
mkdir -p ~/MAT1206E/samplecode
cd ~/MAT1206E/samplecode
wget -nc https://hoanganhduc.github.io/teaching/VNU-HUS/2026/winter/MAT1206E/samplecode/chapter5.zip
```

Extract the ZIP file:

```bash
unzip -o chapter5.zip
```

The ZIP file can also be downloaded directly: [chapter5.zip](https://hoanganhduc.github.io/teaching/VNU-HUS/2026/winter/MAT1206E/samplecode/chapter5.zip).

## Run the sample code

Change to the directory containing the Chapter 5 files before starting PROLOG:

```bash
cd ~/MAT1206E/samplecode/chapter5
```

Enter `halt.` at a PROLOG prompt to exit the current session before loading a different version of a program.

Each SWI-Prolog example below shows two ways to load the program:

1. Start SWI-Prolog and load the file directly with command-line options.
2. Start SWI-Prolog without command-line options, then load the file with `[filename].` at the PROLOG prompt.

In the second method, `?-` is the SWI-Prolog prompt and should not be typed as part of the query.

### Family relationships

#### Method 1: Load the file from the command line

```bash
swipl -q -s rel.pl
```

```prolog
?- child(oscar, X, Y).
```

#### Method 2: Load the file from inside SWI-Prolog

```bash
swipl
```

```prolog
?- [rel].
?- child(oscar, X, Y).
```

Enter `;` to request further answers. Enter `halt.` and start a new session with `rel01.pl`, then with `rel02.pl`, using either of the two methods above. For example, the step-by-step method for `rel01.pl` is:

```prolog
?- [rel01].
?- child(oscar, X, Y).
```

Compare the behavior of the three versions. In `rel.pl`, the recursive definition of `child/3` may continue indefinitely. `rel01.pl` avoids that recursion but does not retain the symmetry of `child/3`; `rel02.pl` uses `child_fact/3` to retain the symmetry without the same recursive definition.

### Maximum and the cut

#### Method 1: Load the file from the command line

```bash
swipl -q -s max.pl
```

```prolog
?- max(3, 2, M).
```

#### Method 2: Load the file from inside SWI-Prolog

```bash
swipl
```

```prolog
?- [max].
?- max(3, 2, M).
```

Enter `halt.` and repeat with `maxwCut.pl`, using either `swipl -q -s maxwCut.pl` or `[maxwCut].`. Compare the definitions with the discussion of the cut operation in Section 5.3.

### Lists and reversal

The predicates in `nrev.pl` call `append/3`, so load `append.pl`, `nrev.pl`, and `accrev.pl` in the same session.

#### Method 1: Load the files from the command line

```bash
swipl -q -g "['append.pl', 'nrev.pl', 'accrev.pl']"
```

```prolog
?- append([a, b], [c, d], L).
?- nrev([a, b, c], R).
?- accrev([a, b, c], [], R).
```

#### Method 2: Load the files from inside SWI-Prolog

```bash
swipl
```

```prolog
?- [append, nrev, accrev].
?- append([a, b], [c, d], L).
?- nrev([a, b, c], R).
?- accrev([a, b, c], [], R).
```

Compare the two implementations of list reversal described in Section 5.4.

### Dynamic predicates

#### Method 1: Load the file from the command line

```bash
swipl -q -s dynamic_rel.pl
```

```prolog
?- descendant(eve, karen).
?- listing(descendant/2).
```

#### Method 2: Load the file from inside SWI-Prolog

```bash
swipl
```

```prolog
?- [dynamic_rel].
?- descendant(eve, karen).
?- listing(descendant/2).
```

The second query displays the `descendant/2` facts inserted by `asserta/1` during the first query.

### Planning

The predicate `plan/4` in `plan.pl` can be called directly after loading the file.

#### Method 1: Load the file from the command line

```bash
swipl -q -s plan.pl
```

```prolog
?- plan(state(left,left,left,left), state(right,right,right,right), [state(left,left,left,left)], Path).
```

#### Method 2: Load the file from inside SWI-Prolog

```bash
swipl
```

```prolog
?- [plan].
?- plan(state(left,left,left,left), state(right,right,right,right), [state(left,left,left,left)], Path).
```

The predicate `start/0` currently calls `write_path/1`, which is not defined in `plan.pl`. To display a generated path with `start.`, replace `write_path(Path).` by:

```prolog
write(Path).
```

Run `start.` and observe the first path. Then try the following version and run `start.` again:

```prolog
write(Path), fail.
```

The second version forces backtracking and displays all generated paths. The file `plan1.pl` already uses `write(Path), fail.`. It can be loaded directly from the command line:

```bash
swipl -q -s plan1.pl
```

```prolog
?- start.
```

Alternatively, load it step by step from inside SWI-Prolog:

```bash
swipl
```

```prolog
?- [plan1].
?- start.
```

### Constraint logic programming

`raumplan.pl` must be run with GNU Prolog.

#### Method 1: Load the file from the command line

```bash
gprolog --consult-file raumplan.pl
```

```prolog
| ?- start.
```

#### Method 2: Load the file from inside GNU Prolog

```bash
gprolog
```

```prolog
| ?- [raumplan].
| ?- start.
```

Compare the result with the room scheduling problem in Example 5.2 and Figure 5.5 of the book.
