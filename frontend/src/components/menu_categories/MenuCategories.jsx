import React from "react";
import styles from "./menuCategories.module.css";
import Image from "next/image";
import Link from "next/link";

export default function MenuCategories() {
  return (
    <div className={styles.container}>
      <div className={styles.about}>
        <div className={styles.imageContainer}>
          <Image src="/shabnam.jpg" alt="" fill className={styles.image} />
        </div>
        <p className={styles.description}>
          Hi every one this is my journey from <b>Iran</b> to <b>canada</b> .
          Hopefully it could be inspiring for people who are trying to
          immigrate.
        </p>
        <Link href="/" className={styles.link}>
          Read More...
        </Link>
      </div>
      <div>
        <span className={styles.categoreisTitle}><b>Interests Categories</b></span>
      </div>
      <div className={styles.categoryList}>
      <Link
          href="/blog?cat=ecology"
          className={`${styles.categoryItem} ${styles.ecology}`}
        >
          Ecology
        </Link>
        <Link
          href="/blog"
          className={`${styles.categoryItem} ${styles.coding}`}
        >
          Coding
        </Link>
        <Link
          href="/blog"
          className={`${styles.categoryItem} ${styles.water}`}
        >
          Water Quality
        </Link>
        <Link
          href="/blog"
          className={`${styles.categoryItem} ${styles.ai}`}
        >
          AI
        </Link>
        <Link
          href="/blog"
          className={`${styles.categoryItem} ${styles.climate}`}
        >
          Climate Change
        </Link>
        <Link
          href="/blog"
          className={`${styles.categoryItem} ${styles.hydrology}`}
        >
          Hydrlogy
        </Link>
      </div>
      <div className={styles.social}>
        <span className={styles.socialTitle}>FOLLOW ME</span>
        <div className={styles.socialItem}>
          <Image src="/facebook.png" alt="facebook" width={24} height={24} />
          <Image src="/instagram.png" alt="instagram" width={24} height={24} />
          <Image src="/linkedin.png" alt="linkedin" width={24} height={24} />
          <Image src="/twitter.png" alt="twitter" width={24} height={24} />
        </div>
      </div>
    </div>
  );
}
