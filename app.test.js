const puppeteer = require('puppeteer');

describe('App Test', () => {
  test('should open the web app and verify the redirect', async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('srikali2009.azurewebsites.net'); // replace with your app url

    // Click on the "Welcome to Google" link
    await page.click('a[href="https://www.google.com"]');

    // Wait for navigation to complete
    await page.waitForNavigation();

    expect(page.url()).toBe('https://www.google.com/');
    await browser.close();
  }, 16000);
});
