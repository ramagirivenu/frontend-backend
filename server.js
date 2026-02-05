const express = require("express");
const dotenv = require("dotenv");

dotenv.config();

const app = express();

// 👇 REQUIRED to read JSON body
app.use(express.json());

// 👇 THIS LINE CONNECTS YOUR ROUTES
const authRoutes = require("./routes/auth.routes");
app.use("/api/v1/auth", authRoutes);

app.listen(5000, () => {
  console.log("Server started on port 5000");
});
