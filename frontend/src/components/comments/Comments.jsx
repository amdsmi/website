"use client";
import React, { useState } from "react";
import styles from "./comments.module.css";
import Link from "next/link";
import Image from "next/image";
import axios from "axios";
import useSWR from "swr";
import Cookies from "js-cookie";
const API_URL = "http://127.0.0.1:5000";

const postData = async (post_id, user_id, description) => {
  const res = await axios.post(API_URL + "/save_comment", {
    post_id: post_id,
    user_id: user_id,
    description: description,
  });

  if (!res.status === 200) {
    throw new Error("Faild");
  }

  return res.data;
};

const fetcher = async (url) => {
  const res = await axios.get(url, {withCredentials:true});

  if (!res.status === 200) {
    throw new Error("Faild");
  }
  return res.data;
};

// const extractCookie = (cookies, name) => {
//   const result = {}
//   cookies.split(';').map(cookie => {var pair = cookie.split("=");
//   result[pair[0].trim()] = pair[1].trim()})
//   return result[name]}

const Comments = ({ post_id }) => {

  const { data, mutate, isLoading } = useSWR(
    `http://127.0.0.1:5000/load_comment?post_id=${post_id}`,
    fetcher
  );
  console.log(data)
  const [description, setDescription] = useState();
  
  const handelSubmit = async () => {
    // const cookiesList = document.cookie
    // console.log(cookiesList)
    // const user_id = extractCookie(cookiesList, 'user_id')
    const user_id = Cookies.get('user_id')
    const resp = await postData(post_id, user_id, description);
    mutate();
  };
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Comments</h1>
      {data?.status === "authenticated" ? (
        <div className={styles.write}>
          <textarea
            placeholder="Write comment..."
            className={styles.input}
            onChange={(e) => setDescription(e.target.value)}
          />
          <button className={styles.button} onClick={handelSubmit}>
            Send
          </button>
        </div>
      ) : (
        <Link href="/login">Login to Write Comment</Link>
      )}
      <div className={styles.Comments}>
        {isLoading
          ? "loading"
          : data?.comment_user?.map((comment) => (
              <div className={styles.comment} key={comment[0]._id}>
                <div className={styles.user}>
                  <Image
                    src={comment[1]?.image}
                    alt=""
                    width={50}
                    height={50}
                    className={styles.image}
                  />
                  <div className={styles.userInfo}>
                    <span className={styles.username}>{comment[1]?.name}</span>
                    <span className={styles.date}>
                      {comment[0]?.date.substring(0, 10)}
                    </span>
                  </div>
                </div>
                <p className={styles.description}>{comment[0]?.description}</p>
              </div>
            ))}
      </div>
    </div>
  );
};

export default Comments;
