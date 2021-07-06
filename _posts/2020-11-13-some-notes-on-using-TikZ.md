---
layout: blog-post
title: Some notes on using TikZ
author: Duc A. Hoang
categories:
  - tex
<!--comment: true-->
description: This post contains some notes of Duc A. Hoang on using TikZ
keywords: TikZ, usage, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This post contains some notes I don't want to forget when using [TikZ](https://github.com/pgf-tikz/pgf). I will keep updating its contents as time goes by. See also [Some TeX Tips]({% link _posts/2018-05-26-some-tex-tips.md %}).

* TOC
{: toc}
</div>

# Resources

* In English
  * [TikZ @ LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX/PGF/TikZ) -- Useful basic TikZ guide.
  * [VisualTikZ](https://ctan.org/pkg/visualtikz).
  * TikZ and PGF [Resources](http://www.texample.net/tikz/resources/) and [Examples](https://texample.net/tikz/).
    * [TikZiT](https://tikzit.github.io/) -- a simple GUI editor that helps drawing with TikZ.
  * Graphics in LaTeX using TikZ, by Zofia Walczak, published in [TUGboat 29:1, 2008](https://www.tug.org/TUGboat/tb29-1/).
  * [tkz-euclide manual](https://ftp.kddilabs.jp/CTAN/macros/latex/contrib/tkz/tkz-euclide/doc/TKZdoc-euclide.pdf).
  * A TikZ tutorial: Generating graphics in the spirit of TeX, by Andrew Mertz and William Slough, published in [TUGboat 30:2, 2009](https://www.tug.org/TUGboat/tb30-2/), see also [the video recording of their talk at TUG 2009 on Youtube](https://www.youtube.com/watch?v=hYjsJVXBlvM).
  * [Graph Theory in LaTeX](https://graphtheoryinlatex.wordpress.com/).
  * [tkz-graph](https://ctan.org/pkg/tkz-graph?lang=en) -- Draw graph-theory graphs.
* In Vietnamese
  * [Vẽ hình khoa học TikZ - Asymptote](http://tikz.vn/).

# Scaling pictures including nodes

```latex
...
\begin{tikzpicture}[scale=0.5, every node/.style={transform shape}]
	% draw your picture here
\end{tikzpicture}
...
```

# Aligning inline TikZ picture

Simply use `[anchor=base, baseline]` option, for example,

```latex
...
\usetikzlibrary{shapes}
...
A rectangle looks like \tikz [anchor=base, baseline, inner sep=0] \node[draw, rectangle, minimum height=2mm] {};
...
```

More details can be found [here](https://tex.stackexchange.com/questions/58419/common-baseline-in-tikz-and-mathmode).

# Define and reuse TikZ pictures

More details can be found [here](https://tex.stackexchange.com/questions/195923/tikz-how-to-create-and-reuse-a-picture).

```latex
...
\tikzset{
	rec1/.pic={
		% draw your rec1 picture here
	}, 
	rec2/.pic={
		% draw your rec2 picture here
	}
	% and so on
}
...
% now we can reuse pictures 
\begin{tikzpicture}
	\pic[color=red]{rec1};
\end{tikzpicture}
...
```

# A simple tree example

I got it from [here](https://texample.net/tikz/examples/tree/). 
Just put here to remember how to draw a tree with TikZ.
More examples can be found [here](https://texample.net/tikz/examples/feature/trees/).

```latex
% A simple Tree
% Author: Stefan Kottwitz
% https://www.packtpub.com/hardware-and-creative/latex-cookbook
\documentclass[border=10pt]{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[sibling distance=10em,
  every node/.style = {shape=rectangle, rounded corners,
    draw, align=center,
    top color=white, bottom color=blue!20}]]
  \node {Formulas}
    child { node {single-line} }
    child { node {multi-line}
      child { node {aligned at}
        child { node {relation sign} }
        child { node {several places} }
        child { node {center} } }
      child { node {first left,\\centered,\\last right} } };
\end{tikzpicture}
\end{document}
```

# New line within a node

Simply specify that the node is a `text` node, like

```latex
...
node[text width=1cm,align=center] {0,1,2\\3,4,5};
...
```

# TikZ matrix for drawing tables

An example taken from [here](https://tex.stackexchange.com/a/18524).

```latex
\documentclass{article}
\usepackage{tikz}
\usetikzlibrary{matrix}
\begin{document}
\begin{tikzpicture}
\matrix [matrix of nodes, ampersand replacement=\&, row sep=-\pgflinewidth,column 2/.style={nodes={rectangle,draw,minimum width=3em}}]
{
	0   \& 6 \\   1   \& 3 \\   
};
\end{tikzpicture}
\end{document}
```

# Positioning elements in a Beamer frame using a grid

An example taken from [this page](https://tex.stackexchange.com/a/269828).

```latex
\documentclass{beamer}
\usepackage{tikz}
\usetikzlibrary{positioning}

\setbeamertemplate{background}{\tikz[overlay, remember picture, help lines]{
    \foreach \x in {0,...,12} \path (current page.south west) +(\x,9.25) node {\small$\x$};
    \foreach \y in {0,...,9} \path (current page.south west) +(12.5,\y) node {\small$\y$};
    \foreach \x in {0,0.5,...,12.5} \draw (current page.south west) ++(\x,0) -- +(0,9.6);
    \foreach \y in {0,0.5,...,9.5} \draw (current page.south west) ++(0,\y) -- +(12.8,0);
  }
}

\begin{document}
\begin{frame}
\begin{tikzpicture}[remember picture, overlay]
    \draw[on grid,solid,red,line width= 1.5pt,-stealth] (current page.south west) -- +(2,2);
\end{tikzpicture}
\end{frame}
\end{document}
```

<div class="figure">
	<img src="https://i.stack.imgur.com/a115Z.png" alt="Showing grid in a Beamer frame" width="60%">
	<br>Showing grid in a Beamer frame
</div>

# Draw an arrow in the middle of the line

An example taken from [this page](https://tex.stackexchange.com/questions/3161/tikz-how-to-draw-an-arrow-in-the-middle-of-the-line).

```latex
\usetikzlibrary{decorations.markings}

\begin{scope}[very thick,decoration={
    markings,
    mark=at position 0.5 with {\arrow{>}}}
    ] 
    \draw[postaction={decorate}] (-4,0)--(4,0);
    \draw[postaction={decorate}] (4,0)--(4,2);
    \draw[postaction={decorate}] (4,2)--(-4,2);
    \draw[postaction={decorate}] (-4,2)--(-4,0);
\end{scope}
```

# Draw edges and paths in the background of nodes

An example from [this page](https://tex.stackexchange.com/a/18201).

```latex
documentclass{article}
\usepackage{tikz}
\usetikzlibrary{backgrounds}

\begin{document}
  \begin{tikzpicture}
    \node [fill=gray!30] (foo) at (0,0) { foo };
    \node [fill=gray!30] (bar) at (2,0) { bar };
    \node [fill=gray!30] (baz) at (4,0) { baz };

    \begin{scope}[on background layer]
        \draw (foo) -- (baz);
    \end{scope}
  \end{tikzpicture}
\end{document}
```

# Adjust figure to fit `\textwidth` using `adjustbox`

An example of using `adjustbox` to adjust the size of a TikZ figure. In this example, I draw the recursion tree of a naive algorithm for computing the 7th [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number); arrows represent recursive calls.

```
\documentclass[class=memoir]{standalone}
\usepackage{tikz}
\usepackage{adjustbox}

\begin{document}
	\begin{adjustbox}{max width=\textwidth}
	\begin{tikzpicture}[every node/.style={draw, rectangle, thick, rounded corners},
	edge from parent/.style={draw, ->, thick},
	level distance=10mm,
	level 1/.style={sibling distance=105mm},
	level 2/.style={sibling distance=56mm},
	level 3/.style={sibling distance=28mm},
	level 4/.style={sibling distance=14mm},
	level 5/.style={sibling distance=7mm}]
		\node {$F_7$}
			child {node {$F_6$}
					child {node {$F_5$}
							child {node {$F_4$}
									child {node {$F_3$}
											child {node {$F_2$}
												child {node {$F_1$}}
												child {node {$F_0$}}
											}
											child {node {$F_1$}}
									}
									child {node {$F_2$}
											child {node {$F_1$}}
											child {node {$F_0$}}
									}
							}
							child {node {$F_3$}
									child {node {$F_2$}
											child {node {$F_1$}}
											child {node {$F_0$}}
									}
									child {node {$F_1$}}
							}
					}
					child {node {$F_4$}
							child {node {$F_3$}
									child {node {$F_2$}
											child {node {$F_1$}}
											child {node {$F_0$}}
									}
									child {node {$F_1$}}
							}
							child {node {$F_2$}
									child {node {$F_1$}}
									child {node {$F_0$}}
							}
					}
			}
			child {node {$F_5$}
					child {node [right=1mm] {$F_4$}
						child {node {$F_3$}
								child {node {$F_2$}
										child {node {$F_1$}}
										child {node {$F_0$}}
								}
								child {node {$F_1$}}
						}
						child {node {$F_2$}
								child {node {$F_1$}}
								child {node {$F_0$}}
						}
					}
					child {node [left=1mm] {$F_3$}
						child {node {$F_2$}
								child {node {$F_1$}}
								child {node {$F_0$}}
						}
						child {node {$F_1$}}
					}
			};
	\end{tikzpicture}
	\end{adjustbox}
\end{document}
```
