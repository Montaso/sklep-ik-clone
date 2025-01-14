package com.example;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.edge.EdgeOptions;
import org.openqa.selenium.safari.SafariDriver;

import com.example.login.LoginHandle;
import com.example.login.RegisterHandle;

public class Main {
    public static void main(String[] args) throws InterruptedException{
        // Create EdgeOptions to customize browser behavior
        EdgeOptions options = new EdgeOptions();
        options.setCapability("acceptInsecureCerts", true); // Bypass SSL errors

        // Initialize the EdgeDriver with the specified options
        WebDriver driver = new EdgeDriver(options);
        driver.get("https://localhost:19323");
        driver.manage().window().maximize();

        new RegisterHandle(driver).run();
        //new LoginHandle(driver).run();
        Thread.sleep(5000);

        //System.out.println("Entering AddToCart operation");
        new AddToCartHandle(driver).run();
        Thread.sleep(5000);

        new CartRemoveHandle(driver).run();
        Thread.sleep(5000);

        new BuyHandle(driver).run();
        Thread.sleep(2000);
        
        new CheckStatusHandle(driver).run();
        //Thread.sleep(5000);

        driver.quit();
    }
}