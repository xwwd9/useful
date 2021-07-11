import Loadable from 'react-loadable';
import Loading from './my-loading-component';

const LoadableComponent = Loadable({
  loader: () => import('./index.js'),
  loading: Loading,
});

export default () => <LoadableComponent />