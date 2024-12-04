package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.safari.SafariDriver;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter @Setter
public class CartRemoveHandle {

    private final String cartLink = "https://localhost:8080/koszyk?action=show";
    private WebDriver driver;

    public CartRemoveHandle(WebDriver driver) {
        this.driver = driver;
    }
    
    public void run() throws InterruptedException {
        driver.get(cartLink);

        driver.findElement(By.className("remove-from-cart")).click();
        Thread.sleep(500);
        driver.findElement(By.className("remove-from-cart")).click();
        Thread.sleep(500);
        driver.findElement(By.className("remove-from-cart")).click();
        Thread.sleep(500);
    }
}
