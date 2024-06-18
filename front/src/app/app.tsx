import React, { useEffect } from 'react';
import styles from './app.module.css';
import { Route, Routes } from 'react-router-dom';
import Navbar from './navbar/navbar';
import Register from './register/register';
import Login from './login/login';
import Users from './users/users';
import Workers from './workers/workers';
import { checkTokenValidity } from '../services/auth';
import Worker from './worker/worker';
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
          <Route path="/worker/:id" element={<Worker />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
