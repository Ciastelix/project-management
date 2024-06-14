// eslint-disable-next-line @typescript-eslint/no-unused-vars
import styles from './app.module.css';

import { Route, Routes } from 'react-router-dom';
import Navbar from './navbar/navbar';
import Register from './register/register';
import Login from './login/login';
import Users from './users/users';
import Workers from './workers/workers';
import React from 'react';

export function App() {
  return (
    <>
      <Navbar />
      <div className={styles['content']}>
        <Routes>
          <Route path="/" element={<div>Home</div>} />
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
