package com.example;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter @Setter
@AllArgsConstructor
public class BuyHandle {
    private final WebDriver driver;
    //private final String cartLink = "https://localhost:8080/koszyk?action=show";
    private final String orderLink = "https://localhost:19323/zam%C3%B3wienie";
    
    private final String addressId = "field-address1";
    private final String postCodeId = "field-postcode";
    private final String cityId = "field-city";

    private final String paymentOptBtn = "payment-option-2";
    private final String conditionsBox = "conditions_to_approve[terms-and-conditions]";

    private final String address = "ul. Kebaba 12";
    private final String postCode = "69-420";
    private final String city = "Gdynia";


    public void run() throws InterruptedException{
        driver.get(orderLink);
        System.out.println("Navigated to: " + orderLink);

        WebElement addressField = driver.findElement(By.id(addressId));
        addressField.sendKeys(address);

        WebElement postCodeField = driver.findElement(By.id(postCodeId));
        postCodeField.sendKeys(postCode);

        WebElement cityField = driver.findElement(By.id(cityId));
        cityField.sendKeys(city);

        Thread.sleep(2000);
        // click 'Next' btn
        driver.findElement(By.name("confirm-addresses")).click();

        Thread.sleep(2000);
        // Select courier (default is clicked so go next)
        driver.findElement(By.name("confirmDeliveryOption")).click();

        Thread.sleep(2000);
        // Select payment method
        driver.findElement(By.id(paymentOptBtn)).click(); 

        // Accept TOS
        driver.findElement(By.id(conditionsBox)).click();

        Thread.sleep(2000);
        // Place an order
        driver.findElement(By.xpath("//button[contains(text(), 'Złóż zamówienie')]")).click();

        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        wait.until(ExpectedConditions.presenceOfElementLocated(By.linkText("pobrać fakturę"))).click();
        
        Thread.sleep(5000);
        //driver.findElement(By.partialLinkText("pobrać fakturę")).click();
    }
}
