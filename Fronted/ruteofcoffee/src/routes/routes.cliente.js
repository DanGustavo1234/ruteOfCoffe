import{ClienteLayout } from '../layouts';
import{Home, Emprendimientos,Emprendedores,Producto} from '../Pages/Cliente/';



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
    {
        path: "/producto",
        layout: ClienteLayout,
        component: Producto,
    },
  

  
];

export default routesCliente;
