# Homework 1

## EX2.
by K4, we have $P(\sim E) = \sim K E \subseteq KP(\sim E) = K (\sim KE)\subseteq \sim KE$ (by K2)
$\implies \sim KE =K(\sim KE)$

## EX3.
- K0/P0
$K\Omega = \Omega \iff K \sim \empty = \sim \empty \iff \sim K \sim \empty = P\empty = \sim\sim \empty = \empty$

- K1/P1
$K(E\cap F) = KE\cap KF \iff K (\sim E)\cap (\sim F) = (K\sim E) \cap (K\sim F)$
$\iff \sim K[(\sim E)\cap (\sim F)] = \sim K[\sim (E\cup F)] = \sim \left[(K\sim E) \cap (K\sim F)\right] = \sim K\sim E \cup \sim K \sim F$
$\iff P(E\cup F) = PE\cup PF$

- K2/P2
$Ke\subseteq E \iff K\sim E\subseteq \sim E \iff \sim K \sim E = PE \supseteq E = \sim\sim E$

- K3/P3
$KE\subseteq E \iff K\sim E \subseteq \sim E \iff \sim K\sim E \supseteq \sim\sim E \iff PE \supseteq E$

- K4/P4
$PE \subseteq KPE \iff P\sim E \subseteq KP\sim E \iff \sim KE \subseteq K\sim KE \iff KE \supseteq \sim K \sim KE = PKE$

## EX4.
a. $K(KE) = KE$ from K3 and thetextbook supplement
b. $K\sim KE = K(P\sim E) \stackrel{P3} = P\sim E = \sim KE$
c. $KPE = PE$ from P4 and textbook supplement
d. $K \sim PE = KK\sim E \stackrel{K3}= K\sim E = \sim PE$

## EX5.



## EX6.
#### a.
a Truism is $\emptyset$

#### b.

$A$ cannot know $\{4, 5\}$ at each event:

from the topic given, we have
- $K_A\{1,2,4,5\} = \{1,2\}$
- $K_A\{2,3,4,5\} = \{3,4,5\}$

$\implies K_A\{2,4,5\} = \empty$
from K2, we can find that if $E_1\subseteq E_2$, then $K E_1 = K (E_1\cap E_2) = K E_1 \cap KE_2 \subseteq E_2$
$\implies K_A \{4,5\}\subseteq K_A \{2,4,5\}=\emptyset$

In other words, $A$ cannot know $\{4,5\}$ whatever the true state is.

#### c.

the possibility set partition of $B$ is
$\{1,2,3\}, \{4,5\}$,

if the true state is located in $\{1,2\}$
- at this state, they can only find the true state located in $P_A\{1,2\}\cap P_B \{1,2\} = \{1,2\}\cap \{1,2,3\} = \{1,2\}$

if the true state is located is $3$
- at this state, $P_A(3)=\{3,4,5\}$, and $B$ will give the information that the true state is located in $P_B(3) = \{1,2,3\}$, then $A$ will find the true state is located in $P_A(3)\cap P_B(3) = \{3\}$.
in other word, $A$ will determine the true state is $3$

if the true state is located in $\{4,5\}$
- they will know the true state is in $P_A\{4,5\}\cap P_B\{4,5\} = \{3,4,5\}\cap \{4,5\} = \{4,5\}$

Therefore, the Possibility set partition of $A$ will become
$\{1,2\}, \{3\}, \{4,5\}$