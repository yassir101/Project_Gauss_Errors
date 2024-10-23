# Project_Gauss_Errors

**Project Overview**

In this project, we explore the solution of linear equation systems using Gauss’s method, a fundamental technique in linear algebra for solving matrix systems. This method is not only crucial for understanding the principles of linear algebra but also serves as the basis for many applications in science and engineering. Specifically, we focus on the LU decomposition of the matrix during the triangulation step, allowing the transformation of the initial system into a simpler format for solving.

**Objective**

Gauss’s method, also known as Gaussian elimination, is often chosen for its robustness and efficiency in handling large systems. However, despite its advantages, the method is not without potential errors, particularly regarding computational errors due to the limitations of computer precision. These errors can significantly affect the reliability of the solutions obtained, especially when numerical stability is compromised by ill-conditioned matrices or arithmetic operations prone to introducing significant rounding errors.

	•	Understand the numerical resolution of linear systems using Gauss’s method.
	•	Analyze error propagation in the context of linear systems.
	•	Study the impact of pivoting strategies and preconditioning on result accuracy.
	•	Use modern debugging tools (GDB) to diagnose and correct coding errors.
	•	Strengthen practical programming skills to improve the reliability of scientific computations.

**Implementation in C**

To address these issues, we have chosen to code this method in the C programming language, a decision motivated by the performance and low-level control it offers, allowing for precise analysis of matrix operations. A key part of our study focuses on observing local errors that appear during the calculation of each term in the matrix transformed by Gauss’s method. The analysis of these errors is performed independently for each matrix element, helping us isolate and understand the specific errors introduced during calculations.

**Debugging and Error Analysis**

To examine these errors in greater detail, we utilize GDB, the GNU Debugger. GDB allows us to not only step through the program execution but also inspect the state of variables and memory at any point in the calculation process. This capability is indispensable for pinpointing where and why numerical errors occur. By understanding these dynamics, we can consider algorithmic improvements or data handling adjustments that reduce the impact of these errors on the final results.

**Conclusion**

Through this project, we aim to gain a deeper understanding of both the theoretical and practical aspects of Gauss’s method, improve our error analysis techniques, and enhance the reliability of numerical solutions in scientific computing.
