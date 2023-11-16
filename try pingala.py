
\textbf{2.8}Suppose we are given a set of n rectangles, denoted $R_1, . . . , R_n$. Each rectangle $R_i$
is specified by four integers $b_i,h_i,l_i,w_i:$
\\
\begin{enumerate}
    \item $b_i$ is the y-coordinate of the base of $R_i$
    \item $h_i > 0$ is the height of $R_i$
    \item $l_i$ is the x-coordinate of the left side of $R_i$
    \item $w_i > 0$ is the width of $R_i$
\end{enumerate}
We want to find a new rectangle R with the smallest area such that it encloses
all n rectangles $R_i
, . . . , R_n$. The sides of the rectangle R will be parallel to
the x- and y-axes. Design and analyze an algorithm that solves this problem
using at most 3n-4 comparisons.\\
\textbf{Solution:}