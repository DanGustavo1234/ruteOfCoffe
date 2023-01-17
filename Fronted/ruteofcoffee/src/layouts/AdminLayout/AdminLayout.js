import React from 'react';

import { LoginAdmin } from '../../Pages';
import './AdminLayout.scss';

export function AdminLayout( props ){
    const { children } = props;
    const auth = null;

    if (!auth) return <LoginAdmin />;

 return (
     <div>
        <h1> Pantalla del administrador</h1>
        {children}
     </div>
    )
}