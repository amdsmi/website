import React from "react";
import styles from "./navbar.module.css";
import Image from "next/image";
import Link from "next/link";
import ThemeToggle from "../theme_toggle/ThemeToggle";
import AuthLink from "../auth_link/AuthLink";

export default function NavBar() {
  return (
    <div className={styles.container}>
      <div className={styles.social}>
        <Image src="/facebook.png" alt="facebook" width={24} height={24} />
        <Image src="/instagram.png" alt="instagram" width={24} height={24} />
        <Image src="/linkedin.png" alt="linkedin" width={24} height={24} />
        <Image src="/twitter.png" alt="twitter" width={24} height={24} />
      </div>
      <div className={styles.logo}>
        <Image
          src="/gold.png"
          alt="shabnam_logo"
          priority={true}
          width={250} 
          height={70}
        ></Image>
      </div>
      <div className={styles.links}>
        <ThemeToggle />
        <Link className={styles.link} href="/">HomePage</Link>
        <Link className={styles.link} href="/">Applications</Link>
        <Link className={styles.link} href="/">About</Link>
        <AuthLink />
      </div>
    </div>
  );
}
