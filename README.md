# Testing_Mutants

## Prerequisites
* To install MutPy (for Mutation testing in Python) you need to run:
  
   ```bash
   pip install mutpy
   ```
* Use this [link](https://www.digitalocean.com/community/tutorials/install-maven-linux-ubuntu) to install Maven (for Mutation testing in Java)


## MutPy (Python)

1. Navigate to the `Code/Python (MutPy)/Unit` directory (MutPy only supports unit testing not integration for integration testing we have manually created mutations).
2. Run the following command in the terminal:

   <!-- ### Unit Mutation -->

   ```bash
   mut.py --target numAnalysis --unit-test tester -m --runner pytest --report-html Output/
    ```
   <!-- ### Integration Mutation

   ```bash
   mut.py --target numAnalysisIntegration --unit-test testerIntegration -m --runner pytest --report-html Integration/ -->
   <!-- ``` -->
4. View the mutation testing results in the corresponding folder by just opening `index.html`.

## PIT (Java)

1. Navigate to the `Code/Java (PIT)/` directory choose either `Unit` or `Integration`.
2. To run the test cases, use:

    ```bash
    mvn package
    ```
3. Run the following command for mutation testing:
    ```bash
    mvn test-compile org.pitest:pitest-maven:mutationCoverage
    ```
4. View the mutation testing results in `target/pit-reports/index.html`.
