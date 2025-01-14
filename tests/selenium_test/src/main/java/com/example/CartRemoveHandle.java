package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter @Setter
@AllArgsConstructor
public class CartRemoveHandle {

    private final String cartLink = "https://localhost:19323/koszyk?action=show";
    private final WebDriver driver;

    public void run() throws InterruptedException {
        driver.get(cartLink);

        driver.findElement(By.className("remove-from-cart")).click();
        Thread.sleep(5000);
        driver.findElement(By.className("remove-from-cart")).click();
        Thread.sleep(5000);
        driver.findElement(By.className("remove-from-cart")).click();
        Thread.sleep(5000);
    }
}
