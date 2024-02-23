import React from "react";
import styles from "./categoryList.module.css";
import Link from "next/link";
import Image from "next/image";
import axios from "axios";
const API_URL = "http://127.0.0.1:5000";

const getData = async () => {
  const res = await axios.get(API_URL + "/categories", { params: {} });

  if (!res.status===200) {
    throw new Error("Faild");
  }

  return res.data;
};

const CategoryList = async () => {
  const data = await getData();
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Ctegories</h1>
      <div className={styles.categories}>
        {data?.map((items) => (
          <Link
            href={`/blog?category=${items['slug']}`}
            className={`${styles.category} ${styles[items.title.split(" ")[0]]}`}
            key={items._id}
          >
            <Image
              src={items.image}
              alt=""
              width={32}
              height={32}
              className={styles.image}
            />

            {items.title}
          </Link>
        ))}
      </div>
    </div>
  );
};

export default CategoryList;
