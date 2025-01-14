package com.example.login;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter @Setter
@AllArgsConstructor
public class RegisterHandle {

    private final WebDriver driver;
    private final String registrationLink = "https://localhost:19323/logowanie?create_account=1";

    private final String firstNameFieldID = "field-firstname";
    private final String lastNameFieldID = "field-lastname";
    private final String emailFieldID = "field-email";
    private final String passwordFieldID = "field-password";

    private final String firstName = "Tomasz";
    private final String lastName = "Siemaszko";
    private final String email = "matip04+aaaaaaa@gmail.com"; // było: 7
    private final String password = "marcinek123";
    
    private final String privacyCheckboxName = "customer_privacy";
    private final String tosCheckboxName = "psgdpr";

    private final String submitButtonClass = "form-control-submit";


    public void run() throws InterruptedException{ 
        driver.get(registrationLink);
        System.out.println("Navigated to: " + registrationLink);

        WebElement firstNameField = driver.findElement(By.id(firstNameFieldID));
        firstNameField.sendKeys(firstName);

        WebElement lastNameField = driver.findElement(By.id(lastNameFieldID));
        lastNameField.sendKeys(lastName);
        
        WebElement emailField = driver.findElement(By.id(emailFieldID));
        emailField.sendKeys(email);

        WebElement passwordField = driver.findElement(By.id(passwordFieldID));
        passwordField.sendKeys(password);


        WebElement privacyCheckbox = driver.findElement(By.name(privacyCheckboxName));
        if (!privacyCheckbox.isSelected()) {
            privacyCheckbox.click();
            System.out.println("Privacy checkbox selected.");
        } else {
            System.out.println("Privacy checkbox was already selected.");
        }

        WebElement tosCheckbox = driver.findElement(By.name(tosCheckboxName));
        if (!tosCheckbox.isSelected()) {
            tosCheckbox.click();
            System.out.println("TOS checkbox selected.");
        } else {
            System.out.println("TOS checkbox was already selected.");
        }
        
        WebElement submitBtn = driver.findElement(By.className(submitButtonClass));
        submitBtn.click();
        System.out.println("Konto zarejestrowane");
    }

}
