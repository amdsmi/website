import React from "react";
import styles from "./singlePage.module.css";
import Image from "next/image";
import Menu from "@/components/Menu/Menu";
import Comments from "@/components/comments/Comments";
import axios from "axios";
const API_URL = "http://127.0.0.1:5000";

const getData = async (post_id) => {
  const res = await axios.get(API_URL + "/post", {
    params: { post_id: post_id },
  });

  if (!res.status === 200) {
    throw new Error("Faild");
  }

  return res.data;
};

const SinglePage = async (params) => {
  const post_id = params.params.slug;
  const data = await getData(post_id);

  const post = data["post"];
  const user = data["user"];
  return (
    <div className={styles.cntainer}>
      <div className={styles.infoContainer}>
        <div className={styles.textContainer}>
          <h1 className={styles.title}>{post?.title}</h1>
          <div className={styles.user}>
            <div className={styles.userImageContainer}>
              <Image src={user?.image} fill alt="" className={styles.avatar} />
            </div>
            <div className={styles.userTextContainer}>
              <span className={styles.username}>{user?.name}</span>
              <span className={styles.date}>{post?.date.substring(0,10)}</span>
            </div>
          </div>
        </div>
        <div className={styles.imageContainer}>
          <Image src={post?.image} fill alt="" className={styles.image} />
        </div>
      </div>
      <div className={styles.content}>
        <div className={styles.post}>
          <div
            className={styles.description}
            dangerouslySetInnerHTML={{ __html: post?.description }}
          />
          <div className={styles.comment}>
            <Comments post_id={post_id} />
          </div>
        </div>
        <Menu />
      </div>
    </div>
  );
};

export default SinglePage;
