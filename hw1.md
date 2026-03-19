# Homework 1

## EX2.
<!-- by K4, we have $P(\sim E) = \sim K E \subseteq KP(\sim E) = K (\sim KE)\subseteq \sim KE$ (by K2)
$\implies \sim KE =K(\sim KE)$ -->
by following exercise, we have $K2\iff P2$ and $K4\iff P4$, therefore, the total axioms we can use are:

K2: $KE\subseteq E$
P2: $E\subseteq PE$
K4: $PE\subseteq KPE$
P4: $PKE\subseteq KE$
<!-- $\implies \sim K \sim E \le K\sim K \sim E$ -->

besides, by $KPE=K(PE)\subseteq PE$ and $PKE=P(KE)\supseteq KE$, we can prove the sign of inequality in K4/P4 can be replaced by sign og equality, and we will directly use the equality relation when we appling K4 or P4 at above calculation.

<!-- $-K^2 E = P(\sim KE)\stackrel{K4}\subseteq $ -->



<!-- --- -->

$KE\stackrel{P2}{\subseteq}PKE \stackrel{P4}= P (PKE) \stackrel{K4}{\subseteq} K(P^2 KE) = KP(PKE) \stackrel{P4}=KPKE\stackrel{P4}=KKE=K^2 E$

$\implies KE \subseteq K^2 E$

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
|people|state of Dirty face|
|-|-|
Alice | 2,5,6,8
Beatrice | 3,5,7,8
Carol|4,6,7,8



initial
|people|partition|
|-|-|
Alice| $\{1, 2\}, \{3,5\}, \{4,6\}, \{7,8\}$
Beatrices|$\{1,3\}, \{2,5\}, \{4,7\}, \{6,8\}$
Carol|$\{1,4\}, \{2,6\}, \{3,7\}, \{5,8\}$




after the broadcast:

|people|partition|
|-|-|
Alice| $\{1\}, \{2\}, \{3,5\}, \{4,6\}, \{7,8\}$
Beatrices|$\{1\},\{3\}, \{2,5\}, \{4,7\}, \{6,8\}$
Carol|$\{1\},\{4\}, \{2,6\}, \{3,7\}, \{5,8\}$

#### after the first second
Alice knowing the partition of B and C
- B blured if and only if the true state is $3$
- C blured if and only if the true state is $4$

Therefore, $A$ can determine if the state is $4$ and $3$ by observing the face of B and C

with the same method, 
- $B$ can determine if the state is $2$ or $4$
- $C$ can determine if the state is $2$ or $3$


Therefore, the partition after 1 second will become
|people|partition|
|-|-|
Alice| $\{1\}, \{2\}, \{3\},\{5\}, \{4\}, \{6\}, \{7,8\}$
Beatrices|$\{1\},\{3\}, \{2\},\{5\}, \{4\},\{7\}, \{6,8\}$
Carol|$\{1\},\{4\}, \{2\},\{6\}, \{3\},\{7\}, \{5,8\}$

#### after the second second
After the first second, $A$ would able to determine all states except $7$ and $8$.
By the information of $B$ and $C$, $A$ will find that
- if the true state is $3,5,7$, then $B$ will blured
- if the true state is $4,6,7$, then $C$ will blured

Therefore, $A$ will able to if the state is $7$ or $8$ by observing the face of $B$ or $C$
Therfore, $A$ will able to distinguish all states after the 2nd second.

The same thinking process will applied to B and C

Therefore, the partition will become as follow:
|people|partition|
|-|-|
Alice| $\{1\}, \{2\}, \{3\},\{5\}, \{4\}, \{6\}, \{7\},\{8\}$
Beatrices|$\{1\},\{3\}, \{2\},\{5\}, \{4\},\{7\}, \{6\},\{8\}$
Carol|$\{1\},\{4\}, \{2\},\{6\}, \{3\},\{7\}, \{5\},\{8\}$

in other words, after 2 seconds, all people will know if their face is dirty.



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