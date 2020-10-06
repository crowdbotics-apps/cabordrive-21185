import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import NotificationList130403Navigator from '../features/NotificationList130403/navigator';
import Settings130402Navigator from '../features/Settings130402/navigator';
import Settings130394Navigator from '../features/Settings130394/navigator';
import UserProfile130392Navigator from '../features/UserProfile130392/navigator';
import BlankScreen0130370Navigator from '../features/BlankScreen0130370/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
NotificationList130403: { screen: NotificationList130403Navigator },
Settings130402: { screen: Settings130402Navigator },
Settings130394: { screen: Settings130394Navigator },
UserProfile130392: { screen: UserProfile130392Navigator },
BlankScreen0130370: { screen: BlankScreen0130370Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
