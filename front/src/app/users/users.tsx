import React, { useState, useEffect } from 'react';
import styles from './users.module.css';
import axios from 'axios';

/* eslint-disable-next-line */
export interface User {
  id: number;
  username: string;
  email: string;
}

const getUsers = async () => {
  try {
    const response = await axios.get('http://localhost:8000/users/');
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.log(error);
  }
};

export function Users() {
  useEffect(() => {
    getUsers().then((data) => {
      setUsers(data);
    });
  }, []);

  const [users, setUsers] = useState<User[]>([]);
  return (
    <div className={styles['container']}>
      <ul>
        {users.map((user) => {
          return (
            <>
              <li>
                {user.username}
                <ul key={user.id}>
                  <li>{user.email}</li>
                  <li>{user.id}</li>
                </ul>
              </li>
            </>
          );
        })}
      </ul>
    </div>
  );
}

export default Users;
