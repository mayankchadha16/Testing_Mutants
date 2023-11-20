# Testing_Mutants

## MutPy (Python)

1. Navigate to the `Code/Python (MutPy)` directory.
2. Run the following command in the terminal:

   ```bash
   mut.py --target numAnalysis --unit-test tester -m --runner pytest
3. View the mutation testing results in the terminal.

## PIT (Java)

1. Navigate to the `Code/Java (PIT)/my-app` directory.
2. To run the test cases, use:

    ```bash
    mvn package
3. Run the following command for mutation testing:
    ```bash
    mvn test-compile org.pitest:pitest-maven:mutationCoverage
4. View the mutation testing results in `target/pit-reports/index.html`.