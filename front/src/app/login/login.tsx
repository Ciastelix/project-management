import React, { useState } from 'react';
import styles from './login.module.css';
import axios from 'axios';
import Cookies from 'js-cookie';
/* eslint-disable-next-line */
export function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  if (Cookies.get('access_token')) {
  }
  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    const formData = {
      username: username,
      password: password,
    };
    const config = {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    };
    axios
      .post('http://localhost:8000/users/login', formData, config)
      .then((response) => {
        Cookies.set('access_token', response.data.access_token);
        window.location.href = 'http://localhost:4200/';
        axios
          .get('http://localhost:8000/users/me/token', {
            headers: {
              Authorization: `bearer ${Cookies.get('access_token')}`,
            },
          })
          .then((res) => {
            console.log(res.data.id);
          })
          .catch((error) => {
            console.log(error);
          });
      })
      .catch((error) => {
        console.log(error);
        setPassword('');
      });
  };
  return (
    <div className={styles['container']}>
      <form onSubmit={handleSubmit} className={styles['login-form']}>
        <label htmlFor="username" className={styles['form-label']}>
          Username:
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className={styles['form-input']}
          />
        </label>
        <label htmlFor="password" className={styles['form-label']}>
          Password:
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className={styles['form-input']}
          />
        </label>
        <button type="submit" className={styles['submit-button']}>
          Login
        </button>
      </form>
    </div>
  );
}

export default Login;
