const express = require('express');
 const app = express();
 const port = 3000;
 
 app.get('/products', (req, res) => {
     res.json({ id: 101, name: "Laptop", price: 999 });
     try {
         res.json({ id: 101, name: "Laptop", price: 999 });
     } catch (error) {
         res.status(500).json({ error: "Product Service failed" });
     }
 });
 
 app.listen(port, () => {
     console.log(`Product Service running on port ${port}`);
 });
