param (
    [string]$Arg1, # email,
    [string]$Arg2 # shouldBuy
)

java -jar out/artifacts/selenium_test_jar/selenium_test.jar $Arg1 $Arg2