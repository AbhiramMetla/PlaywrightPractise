from playwright.sync_api import Playwright
ordersPayLoad =  {"orders":[{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}

class APIUtils:

    def getToken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_context.post("/api/ecom/auth/login",
                                 data = {"userEmail": "abhi123456789@gmail.com", "userPassword": "Naga@123"})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]


    def createOrder(self, playwright:Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url = "https://rahulshettyacademy.com/client")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data = ordersPayLoad,
                                            headers = {"Authorization": token,
                                                       "Content-Type": "application/json",
                                                       })
        print(response.json())
        responseBody = response.json()
        orderId = responseBody["orders"][0]
        return orderId