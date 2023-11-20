# Testing_Mutants

## Prerequisites
* To install MutPy (for Mutation testing in Python) you need to run:
  
   ```bash
   pip install mutpy
   ```
* Use this [link](https://www.digitalocean.com/community/tutorials/install-maven-linux-ubuntu) to install Maven (for Mutation testing in Java)


## MutPy (Python)

1. Navigate to the `Code/Python (MutPy)` directory.
2. Run the following command in the terminal:

   ```bash
   mut.py --target numAnalysis --unit-test tester -m --runner pytest --report-html ./
3. View the mutation testing results in he same folder by just opening `index.html`.

## PIT (Java)

1. Navigate to the `Code/Java (PIT)/my-app` directory.
2. To run the test cases, use:

    ```bash
    mvn package
3. Run the following command for mutation testing:
    ```bash
    mvn test-compile org.pitest:pitest-maven:mutationCoverage
4. View the mutation testing results in `target/pit-reports/index.html`.
