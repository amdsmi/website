import React from "react";
import styles from "./featured.module.css";
import Image from "next/image";
import { Syne_Tactile } from "next/font/google";

export default function Featured() {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}> Hey, This is </h1>
      <h1 className={styles.title}>
        {" "}
        <b>Shabnam Majnooni</b>{" "}
      </h1>
      <h1 className={styles.title}> offcial website</h1>
      <div className={styles.post}>
        <div className={styles.imgContainer}>
          <Image
            src="/tree.jpg"
            alt=""
            fill
            className={styles.image}
            priority={true}
          />
        </div>
        <div className={styles.textContainer}>
          <h1 className={styles.postTitle}>
            Lorem ipsum dolor, sit amet consectetur adipisicing elit.
          </h1>
          <p className={styles.postDescription}>
            Culpa labore iste velit vero saepe quibusdam dolore magnam laborum,
            officia repellendus incidunt quia fugiat praesentium molestias
            ipsum! Voluptatibus enim iure consequatur!
          </p>
          <button className={styles.button}>Read More</button>
        </div>
      </div>
    </div>
  );
}
