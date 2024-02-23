import React from "react";
import styles from "./cardList.module.css";
import Pagination from "../pagination/Pagination";
import Card from "../card/Card";
import axios from "axios";
const API_URL = "http://127.0.0.1:5000";
const POST_PER_PAGE = 5;

const getData = async (page, category) => {
  const res = await axios.get(API_URL + "/posts", {
    params: {
      'page': page,
      'postPerPage': POST_PER_PAGE,
      'category': category || "",
    },
    
  });

  if (!res.status === 200) {
    throw new Error("Faild");
  }

  return res.data;
};

const CardList = async ({ pageNum, category}) => {
  const data = await getData(pageNum, category);
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Recent Posts</h1>
      <div className={styles.posts}>
        {data["posts"]?.map((post) => (
          <Card post={post} key={post._id} />
        ))}
      </div>
      <Pagination category={category} page={pageNum} previous={data["previous"]} next={data["next"]} />
    </div>
  );
};

export default CardList;
