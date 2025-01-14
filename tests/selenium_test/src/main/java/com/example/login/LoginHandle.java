package com.example.login;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter @Setter
@AllArgsConstructor
public class LoginHandle {
    
    private final WebDriver driver;
    private final String loginLink = "https://localhost:19323/logowanie?back=my-account";

    private final String emailId = "field-email";
    private final String passwordId = "field-password";
    private final String submitId = "submit-login";

    private final String email = "matip04@gmail.com";
    private final String password = "marcinek123";

    public void run() throws InterruptedException {
        driver.get(loginLink);

        WebElement emailField = driver.findElement(By.id(emailId));
        emailField.sendKeys(email);

        WebElement passwordField = driver.findElement(By.id(passwordId));
        passwordField.sendKeys(password);

        driver.findElement(By.id(submitId)).click();


    }
}
