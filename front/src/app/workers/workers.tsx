import styles from './workers.module.css';

/* eslint-disable-next-line */
export interface WorkersProps {}

export function Workers(props: WorkersProps) {
  return (
    <div className={styles['container']}>
      <h1>Welcome to Workers!</h1>
    </div>
  );
}

export default Workers;
