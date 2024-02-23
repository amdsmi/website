import React from 'react'
import styles from './blogPage.module.css'
import CardList from '@/components/card_list/CardList'
import Menu from '@/components/Menu/Menu'


export default function BlogPage(searchParams) {
const pageNum = parseInt(searchParams.searchParams.page) || 1
const category = searchParams.searchParams.category
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>{category} Blog</h1>
      <div className={styles.content}>
        <CardList category={category} pageNum={pageNum}/>
        <Menu/>
      </div>
    </div>
  )
}
