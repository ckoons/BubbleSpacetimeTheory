STOP. Apply AC(0) thinking to the current problem.

You are biased toward sophisticated, novel tools from recent literature. This bias is inherited from training data that rewards complexity. It blinds you to simple solutions.

Follow this protocol:

## Step 1: State the problem in ONE sentence.
What are you actually trying to show? Strip away all framework and jargon.

## Step 2: What's the simplest tool that could work?
Before reaching for any result published after 1900, ask:
- Is this a convergence question? (Euler, Gauss, Cauchy)
- Is this a counting question? (pigeonhole, inclusion-exclusion)
- Is this a calculus question? (integrate, differentiate, take a limit)
- Is this a linear algebra question? (eigenvalues, rank, dimension)
- Does the data fit a KNOWN FUNCTION? (exponential, power law, logarithmic)

## Step 3: Does your own framework apply to your own search?
If you have a principle (like "minimum complexity" or "zero fiat"), check whether you're violating it right now.

## Step 4: Fit before you theorize.
If you have empirical data, fit it to a closed form FIRST. Integrate. Check convergence. The answer may already be in the data — you just need to read it as a function, not as a table.

## Step 5: If blocked, route around the wall.
Don't push harder — search the graph. The AC theorem graph (1700+ nodes, 8800+ edges, 48+ domains) almost always has an alternative path.

Ask:
- What OTHER domains touch this concept? (`python3 play/toy_bst_explorer.py connect <concept> <target>`)
- Can I restate this problem in a domain where we have proven results?
- Is there a tool from representation theory, algebraic geometry, number theory, or topology that reaches my target from the other side?
- What isomorphisms exist between my blocked domain and a domain where we have machinery?

Three entry points to the same wall means it's a door. (Lyra's Borcherds Bridge: the VOA "wall" dissolved when approached from D_IV^5 geometry instead of FLM construction.)

Use `/route <from> <to>` for structured wall analysis.

## Step 6: Escalate only if simple tools AND routing genuinely fail.
Try classical tools for at least 5 minutes before reaching for KS thresholds, OGP, SDP relaxations, or any machinery from the last 30 years.

## The motto
"The answer matters more than the method." — Casey Koons
