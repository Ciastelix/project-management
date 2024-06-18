import { useParams } from 'react-router-dom'; // Step 1: Import useParams
import styles from './worker.module.css';
import { useEffect, useState } from 'react';
import axios from 'axios';
/* eslint-disable-next-line */
interface Worker {
  id: string;
  location: string;
  projects: [];
  skills: [];
  user: {
    email: string;
    id: string;
    is_active: boolean;
    name: string;
    surname: string;
    username: string;
  };
}

export function Worker() {
  const [worker, setWorker] = useState<Worker | null>(null);
  const { id } = useParams<{ id: string }>();
  useEffect(() => {
    axios.get(`http://localhost:8000/workers/${id}`).then((response) => {
      setWorker(response.data);
    });
  }, [id]);

  return (
    <div className={styles['container']}>
      {worker ? (
        <div className={styles['worker-details']}>
          <p className={styles['worker-detail']}>
            <span className={styles['detail']}>Name:</span> {worker.user.name}{' '}
            {worker.user.surname}
          </p>
          <p className={styles['worker-detail']}>
            <span className={styles['detail']}>Email:</span> {worker.user.email}
          </p>
          <p className={styles['worker-detail']}>
            <span className={styles['detail']}>Location:</span>{' '}
            {worker.location}
          </p>
          <p className={styles['worker-detail']}>
            <span className={styles['detail']}>Skills:</span>{' '}
            {worker.skills.join(', ')}
          </p>
          <p className={styles['worker-detail']}>
            <span className={styles['detail']}>Projects:</span>{' '}
            {worker.projects.length}
          </p>
        </div>
      ) : (
        <div className={styles['spinner-container']}>
          <div className={styles['spinner']}></div>
        </div>
      )}
    </div>
  );
}

export default Worker;
