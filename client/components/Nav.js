import React from 'react'
import { Link } from 'react-router-dom'

import css from '../css'

export default function Nav() {
  return (
    <header className={css.navbar.outer}>
      <section>
        <Link to="/" className={css.navbar.brand}>
          Prevpoint Forms
        </Link>
      </section>
      <section className="flex items-center">
        <Link to="/app/form-mapper/">Form Mapper</Link>
      </section>
    </header>
  )
}
