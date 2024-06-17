import React, { useEffect, useState } from 'react';
import Cookies from 'js-cookie';
import styles from './app.module.css';
import axios from 'axios';
import { Route, Routes } from 'react-router-dom';
import Navbar from './navbar/navbar';
import Register from './register/register';
import Login from './login/login';
import Users from './users/users';
import Workers from './workers/workers';
import { checkTokenValidity } from '../services/auth';
export function App() {
  useEffect(() => {
    checkTokenValidity();
  }, []);
  return (
    <>
      <Navbar />
      <div className={styles['content']}>
        <Routes>
          <Route path="/" element={<></>} />
          <Route path="/users" element={<Users />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/workers" element={<Workers />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
