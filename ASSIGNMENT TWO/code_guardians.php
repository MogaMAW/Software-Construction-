<?php
// Example code for handling user authentication
class Authentication {
    public function login($username, $password) {
        // Authentication logic
        if ($username === "admin" && $password === "admin") {
            return "Login successful";
        } else {
            return "Invalid credentials";
        }
    }
    
    public function register($username, $password, $email) {
        // Registration logic
        if (strlen($password) < 8) {
            return "Password must be at least 8 characters long";
        } else {
            return "User registered successfully";
        }
    }
    
    // Other methods...
}
?>