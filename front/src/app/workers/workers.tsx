import styles from './workers.module.css';
import axios from 'axios';
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

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

export function Workers() {
  const [workers, setWorkers] = useState<Worker[]>([]);
  const [showActive, setShowActive] = useState<boolean | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    axios
      .get('http://localhost:8000/workers')
      .then((response) => {
        setWorkers(response.data);
      })
      .catch((error) => {
        console.error('Error fetching workers:', error);
      });
  }, []);

  const filteredWorkers = workers.filter(
    (worker) => showActive === null || worker.user.is_active === showActive
  );

  const handleCardClick = (id: string) => {
    navigate(`/worker/${id}`);
  };

  return (
    <>
      <div className={styles['button-container']}>
        <button className={styles.button} onClick={() => setShowActive(null)}>
          Show All
        </button>
        <button className={styles.button} onClick={() => setShowActive(true)}>
          Show Active
        </button>
        <button className={styles.button} onClick={() => setShowActive(false)}>
          Show Inactive
        </button>
      </div>
      <div className={styles['container']}>
        {filteredWorkers.length > 0 ? (
          <>
            {filteredWorkers.map((worker) => (
              <div
                className={styles['card']}
                key={worker.id}
                onClick={() => handleCardClick(worker.id)}
                style={{ cursor: 'pointer' }}
              >
                <h2 className={styles['card-name']}>
                  {worker.user.name} {worker.user.surname}
                </h2>
                <p>Email: {worker.user.email}</p>
                <p>Skills: {worker.skills.join(', ')}</p>
              </div>
            ))}
          </>
        ) : (
          <p className={styles['no-workers']}>No workers found.</p>
        )}
      </div>
    </>
  );
}

export default Workers;
