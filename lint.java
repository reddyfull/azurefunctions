def SonarLintTest():

    # This line of code will cause a SonarLint warning because it is using a deprecated method.
    print("This is a deprecated method.")

    # This line of code will cause a SonarLint error because it is using a hardcoded password.
    password = "password"
    print("This is a hardcoded password.")

if __name__ == "__main__":
    SonarLintTest()
