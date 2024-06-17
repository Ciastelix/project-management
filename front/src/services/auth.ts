import axios from 'axios';
import Cookies from 'js-cookie';
import React, { useEffect, useState } from 'react';

export const checkTokenValidity = async () => {
  const [isTokenValid, setIsTokenValid] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  const token = Cookies.get('access_token');
  if (!token) {
    window.location.href = '/login';
    return;
  }

  try {
    await axios
      .get('http://localhost:8000/users/me/token', {
        headers: {
          Authorization: `bearer ${Cookies.get('access_token')}`,
        },
      })
      .then((res) => {
        console.log(res);
        setIsTokenValid(res.data.isValid);
      })
      .catch((error) => {
        console.log(error);
      });
  } catch (error) {
    console.error('Error validating token:', error);
  } finally {
    setIsLoading(false);
  }

  if (!isTokenValid) {
    window.location.href = '/login';
  }
};
