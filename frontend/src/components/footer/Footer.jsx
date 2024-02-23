import React from "react";
import styles from "./footer.module.css";
import Image from "next/image";
import Link from "next/link";

export default function Footer() {
  return (
    <div className={styles.container}>
      <div className={styles.info}>
        <div className={styles.logo}>
          <Image src="/gold.png" alt="" width={300} height={100} />
        </div>
        <p className={styles.descroption}>
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officia
          aliquid quibusdam odio esse atque animi sunt qui? Quod tempore
          reiciendis perferendis molestias ipsum, deleniti vel repellat numquam
          veritatis iure voluptates.
        </p>
        <div className={styles.icons}>
          <Image src="/facebook.png" alt="facebook" width={24} height={24} />
          <Image src="/instagram.png" alt="instagram" width={24} height={24} />
          <Image src="/linkedin.png" alt="linkedin" width={24} height={24} />
          <Image src="/twitter.png" alt="twitter" width={24} height={24} />
        </div>
      </div>
      <div className={styles.links}>
        <div className={styles.list}>
          <span className={styles.listTitle}>Links</span>
          <Link href='/'>Home Page</Link>
          <Link href='/'>Application</Link>
          <Link href='/'>About</Link>
          <Link href='/'>Contact</Link>
        </div>
        <div className={styles.list}>
          <span className={styles.listTitle}>Tags</span>
          <Link href='/'>AI</Link>
          <Link href='/'>Ecology</Link>
          <Link href='/'>Hydrology</Link>
          <Link href='/'>coding</Link>
        </div>
        <div className={styles.list}>
          <span className={styles.listTitle}>Social</span>
          <Link href='/'>Instagram</Link>
          <Link href='/'>LinkedIn</Link>
          <Link href='/'>Twitter</Link>
          <Link href='/'>FaceBook</Link>
        </div>
      </div>
    </div>
  );
}
