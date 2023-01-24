import{ClienteLayout } from '../layouts';
import{Home, Emprendimientos,Emprendedores } from '../Pages/Cliente';


const routesCliente = [
    {
        path: "/",
        layout: ClienteLayout,
        component: Home,
    },
    {
        path: "/emprendimientos",
        layout: ClienteLayout,
        component: Emprendimientos,
    },
    {
        path: "/emprendedores",
        layout: ClienteLayout,
        component: Emprendedores,
    },
];

export default routesCliente;
