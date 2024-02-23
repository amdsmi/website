import React from "react";
import styles from "./card.module.css";
import Image from "next/image";
import Link from "next/link";

export default function Card({key, post}) {
  return (
    <div className={styles.container} key={key}>
      <div className={styles.imageContainer}>
        <Image src={post.image} alt="" fill className={styles.image}/>
      </div>
      <div className={styles.textContainer}>
        <div className={styles.details}>
          <span className={styles.date}>{post.date.substring(0,11)} </span>
          <span className={styles.category}>{post.categories}</span>
        </div>
        <Link href={`posts/${post._id}`}>
          <h1>{post.title}</h1>
        </Link>
        <div className={styles.description} dangerouslySetInnerHTML={{ __html: post?.description.substring(0,60) }}/>
        <Link href={`posts/${post._id}`} className={styles.link}>Read More...</Link>
      </div>
    </div>
  );
}
