"use client";
import React from "react";
import style from "./pagination.module.css";
import { useRouter } from "next/navigation";

export default function Pagination({ category, page, previous, next }) {
  const router = useRouter();

  return (
    <div className={style.container}>
      <button
        disabled={previous}
        className={style.button}
        onClick={() => {
          router.push(
            category
              ? `/blog?category=${category}&page=${page - 1}`
              : `?page=${page - 1}`
          );
        }}
      >
        Previous
      </button>

      <button
        disabled={next}
        className={style.button}
        onClick={() => {
          router.push(
            category
              ? `/blog?category=${category}&page=${page + 1}`
              : `?page=${page + 1}`
          );
        }}
      >
        Next
      </button>
      
    </div>
  );
}
