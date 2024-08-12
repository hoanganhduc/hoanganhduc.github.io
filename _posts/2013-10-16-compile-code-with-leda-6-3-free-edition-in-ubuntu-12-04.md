---
layout: blog-post
title: Compile code with LEDA 6.3 Free Edition in Ubuntu 12.04
author: Duc A. Hoang
categories:
  - "linux"
comment: true
last_modified_at: 2024-03-12
description: This post describes how to compile code with LEDA 6.3 Free Edition in Ubuntu 12.04
keywords: ubuntu, LEDA, compilation
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
LEDA is [AlgoSol](https://www.algorithmic-solutions.com)'s C++ class library for efficient data types and algorithms. LEDA provides algorithmic in-depth knowledge in the field of graph and network problems, geometric computations, combinatorial optimization and other. It offers a huge number of relevant algorithms in an easy-to-use and efficient form. The free edition of LEDA can be found [here](https://www.algorithmic-solutions.com/index.php/products/leda-free-edition). This post describes how to compile code with LEDA 6.3 Free Edition in Ubuntu 12.04.
</div>

To compile a file `example.cpp` with the LEDA directory extracted to the `$HOME` directory, in terminal, type

```bash
export LEDAROOT=$HOME/LEDA
export LD_LIBRARY_PATH=$LEDAROOT
g++ -I$LEDAROOT/incl -L$LEDAROOT example.cpp -lleda -lX11 -lm -o example
```
