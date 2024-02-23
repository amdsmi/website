import Image from "next/image";
import Link from "next/link";
import React from "react";
import styles from "./menuPosts.module.css";

export default function MenuPosts({ withImage }) {
  return (
    <div className={styles.items}>
      <Link href="/" className={styles.item}>
        {withImage && (
          <div className={styles.imageContainer}>
            <Image src="/1.jpg" alt="" className={styles.image} fill />
          </div>
        )}
        <div className={styles.textContainer}>
          <span className={`${styles.category} ${styles.hydrology}`}>
            Hydrology
          </span>
          <h3 className={styles.postTitle}>
            Lorem ipsum dolor sit amet consectetur.
          </h3>
          <div className={styles.detail}>
            <span className={styles.username}>Ahmad Saremi</span>
            <span className={styles.date}> - 10.11.2023</span>
          </div>
        </div>
      </Link>
      <Link href="/" className={styles.item}>
        {withImage && (
          <div className={styles.imageContainer}>
            <Image src="/1.jpg" alt="" className={styles.image} fill />
          </div>
        )}
        <div className={styles.textContainer}>
          <span className={`${styles.category} ${styles.ai}`}>AI</span>
          <h3 className={styles.postTitle}>
            Lorem ipsum dolor sit amet consectetur.
          </h3>
          <div className={styles.detail}>
            <span className={styles.username}>Ahmad Saremi</span>
            <span className={styles.date}> - 10.11.2023</span>
          </div>
        </div>
      </Link>
      <Link href="/" className={styles.item}>
        {withImage && (
          <div className={styles.imageContainer}>
            <Image src="/1.jpg" alt="" className={styles.image} fill />
          </div>
        )}
        <div className={styles.textContainer}>
          <span className={`${styles.category} ${styles.coding}`}>Coding</span>
          <h3 className={styles.postTitle}>
            Lorem ipsum dolor sit amet consectetur.
          </h3>
          <div className={styles.detail}>
            <span className={styles.username}>Ahmad Saremi</span>
            <span className={styles.date}> - 10.11.2023</span>
          </div>
        </div>
      </Link>
    </div>
  );
}
